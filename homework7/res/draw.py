import matplotlib.pyplot as plt
import numpy as np
loss = []
acc = []
epoch = []
with open(r'D:\Users\53263\courses\ai_design\homework7\train copyresnet18.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        s = line.strip().split()
        loss.append(float(s[4].split(':')[-1]))
        acc.append(float(s[-1].split(':')[-1]))
        epoch.append(int(s[0].split(':')[-1]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(epoch[:158],acc[:158], '-', label = 'acc')
ax2 = ax.twinx()
ax2.plot(epoch[:158],loss[:158], '-r', label = 'loss')
ax.legend(loc = 0)
ax.grid()
ax.set_xlabel("epoch")
ax.set_ylabel(r"acc (%)")
ax2.set_ylabel(r"loss")
ax2.set_ylim(0.000600, 0.020)
ax.set_ylim(30,100)
ax2.legend(loc = 2)
plt.show()

