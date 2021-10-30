from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import argparse
plt.ion()   

parser = argparse.ArgumentParser(description='PyTorch CIFAR Training')
parser.add_argument('--data', default='data', type=str, help='Dataset directory')
parser.add_argument('--dataset', default='cifar10', type=str, help='Dataset name')
parser.add_argument('--lr-type', default='SGDR', type=str, help='learning rate strategy')
parser.add_argument('--gpu-id', type=str, default='0')
parser.add_argument('--manual_seed', type=int, default=0)
parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
parser.add_argument('--evaluate', '-e', action='store_true', help='evaluate model')

parser.add_argument('--init-lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--milestones', default=[150, 225], type=list, help='milestones for lr-multistep')
parser.add_argument('--sgdr-t', default=10, type=int, dest='sgdr_t',help='SGDR T_0')
parser.add_argument('--epochs', type=int, default=1270, help='number of epochs to train')

# global hyperparameter set
args = parser.parse_args()


num_classes = 10
trainset = torchvision.datasets.CIFAR10(root=args.data, train=True, download=True,
                                        transform=transforms.Compose([
                                            transforms.RandomCrop(32, padding=4),
                                            transforms.RandomHorizontalFlip(),
                                            transforms.ToTensor(),
                                            transforms.Normalize([0.49139968, 0.48215827, 0.44653124],
                                                                [0.24703233, 0.24348505, 0.26158768])
                                        ]))
testset = torchvision.datasets.CIFAR10(root=args.data, train=False, download=True,
                                        transform=transforms.Compose([
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.49139968, 0.48215827, 0.44653124],
                                                                [0.24703233, 0.24348505, 0.26158768]),]))


trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True,
                                          pin_memory=(torch.cuda.is_available()))

testloader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False,
                                         pin_memory=(torch.cuda.is_available()))


use_gpu = torch.cuda.is_available()


def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  



inputs, classes = next(iter(trainloader))


out = torchvision.utils.make_grid(inputs)

# imshow(out, title=[class_names[x] for x in classes])



def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        
        # for phase in ['train', 'val']:
        #     if phase == 'train':
        #         scheduler.step()
        #         model.train(True)  
        #     else:
        #         model.train(False)  

        running_loss = 0.0
        running_corrects = 0

        
        for data in trainloader:
            
            inputs, labels = data

            
            if use_gpu:
                inputs = Variable(inputs.cuda())
                labels = Variable(labels.cuda())
            else:
                inputs, labels = Variable(inputs), Variable(labels)

            
            optimizer.zero_grad()

            
            outputs = model(inputs)
            _, preds = torch.max(outputs.data, 1)
            loss = criterion(outputs, labels)

            
            loss.backward()
            optimizer.step()

            
            running_loss += loss.data[0] * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)

        epoch_loss = running_loss / 50000
        epoch_acc = running_corrects / 50000

        print('{} Loss: {:.4f} Acc: {:.4f}'.format(
             epoch_loss, epoch_acc))


        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    
    model.load_state_dict(best_model_wts)
    return model




def visualize_model(model, num_images=6):
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig = plt.figure()

    for i, data in enumerate(testloader):
        inputs, labels = data
        if use_gpu:
            inputs, labels = Variable(inputs.cuda()), Variable(labels.cuda())
        else:
            inputs, labels = Variable(inputs), Variable(labels)

        outputs = model(inputs)
        _, preds = torch.max(outputs.data, 1)

        for j in range(inputs.size()[0]):
            images_so_far += 1
            ax = plt.subplot(num_images//2, 2, images_so_far)
            ax.axis('off')
            # ax.set_title('predicted: {}'.format(class_names[preds[j]]))
            imshow(inputs.cpu().data[j])

            if images_so_far == num_images:
                model.train(mode=was_training)
                return
    model.train(mode=was_training)



model_ft = models.resnet18(pretrained=True)
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 2)

if use_gpu:
    model_ft = model_ft.cuda()

criterion = nn.CrossEntropyLoss()


optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)


exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)



model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler,
                       num_epochs=25)



visualize_model(model_ft)
