import numpy as np
import pandas as pd
from sklearn import preprocessing
import sklearn
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,accuracy_score,confusion_matrix
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def data_process(feature:np):
    for idx_i,i in enumerate(feature):
        num = 0
        count = 0
        for idx_j,j in enumerate(i):
            try:
                num += int(j)
                feature[idx_i][idx_j] = int(j)
                count += 1
            except:
                continue
        num = num/count
        for idx_j,j in enumerate(i):
            if isinstance(j,int) == False:
                feature[idx_i][idx_j] = int(num)
    
    return feature
            

def label_process(label):
    for i in range(len(label)):
        if int(label[i]) == 2:
            label[i] = 1
        else:
            label[i] = 0
    return label

def sigmoid(x):
    return 1 / (1+np.exp(-x))

class lr():
    def __init__(self,X,Y,lr,num_arg):
        self.X = np.mat(X)
        self.Y = np.mat(Y)
        self.rate = lr
        self.final_w = 0
        self.num_arg = num_arg
    def train(self):
        w = np.ones((self.num_arg,1))
        iterater = 0
        while iterater<=50:
            h = sigmoid(self.X * w)
            # import pdb;pdb.set_trace()
            w += self.rate*self.X.T*(self.Y - h)

            iterater += 1
        self.final_w = w
        # print(self.final_w)
    def pred(self,x_test):
        x_test = np.mat(x_test)
        return sigmoid(x_test * self.final_w)
    def eval(self,y_pred,y_true):
        y_true = np.array(y_true)
        num = 0
        for i in range(len(y_pred)):
            # import pdb;pdb.set_trace()
            if int(y_pred[i]>=0.5) == y_true[i]:
                num += 1
        print('Written by myself:')
        print('score:',num/len(y_true))
        print('error rates:',1-num/len(y_true))
        
def sklearn_lr(X_train,X_test,y_train,y_test):
    cls = LogisticRegression()
    cls.fit(X_train,y_train)
    y_pred = cls.predict(X_test)
    print('Sklearn:')
    print('score:',accuracy_score(y_test,y_pred))
    print('error rates:',1-accuracy_score(y_test,y_pred))


if __name__ == '__main__':
    data = pd.read_csv(r'dataset\breast-cancer-wisconsin.data')
    data = np.array(data)
    x = data[:,1:-1]
    y = data[:,-1].reshape(-1,1)
    x = data_process(x)
    x = x.astype('float')
    y = y.astype('float')
    y = label_process(y)
    X_train,X_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=66)
    # import pdb;pdb.set_trace()
    X_train = np.insert(X_train, 0, 1, axis=1)
    X_test = np.insert(X_test, 0, 1, axis=1)



    ss_X = StandardScaler()  
    ss_y = StandardScaler()
    X_train = ss_X.fit_transform(X_train)            
    X_test  = ss_X.transform(X_test)

    sklearn_lr(X_train,X_test,y_train,y_test)
    
    cls = lr(X_train,y_train,0.01,len(X_train[0]))
    cls.train()
    y_pred = cls.pred(X_test)
    cls.eval(y_pred,y_test)
