from time import time
import numpy as np
import copy
def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j],end = ' ')
        print()
class use_numpy():
    def __init__(self):
        pass
    def add(self,a,b):
        a = np.mat(a)
        b = np.mat(b)
        return a+b
    def sub(self,a,b):
        a = np.mat(a)
        b = np.mat(b)
        return a-b
    def mul(self,a,b):
        a = np.mat(a)
        b = np.mat(b)
        return a.dot(b)
    def divide(self,a,b):
        a = np.mat(a)
        b = np.mat(b)
        return a/b
    def transpose(self,a):
        a = np.mat(a)
        return a.T

class without_numpy():
    def __init__(self):
        pass      

    def expend(self,a:list):
        b = copy.deepcopy(a)
        m = len(b)
        n = len(b[0])
        if m == 1:
            for i in range(n-1):
                b.append(b[0].copy()) # 注意！！！不能直接append(b[0]),要浅拷贝。
        if n == 1:
            for i in range(m-1):
                for i in range(m):
                    b[i].append(b[i][0])
        return b
     

    def add(self,a,b):
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c = copy.deepcopy(a)
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] += b[i][j]
            return c
        else:
            c = self.expend(a)
            d = self.expend(b)
            try:
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        c[i][j] += d[i][j]
                return c
            except:
                print('a和b形状不匹配')                   
    def sub(self,a,b):
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c = copy.deepcopy(a)
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] -= b[i][j]
            return c
        else:
            c = self.expend(a)
            d = self.expend(b)
            try:
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        c[i][j] -= d[i][j]
                return c
            except:
                print('a和b形状不匹配') 
    def add_1(self,a,b):
        num = 0
        for i in range(len(a)):
                num += a[i]*b[i]
        return num
    def mul(self,a,b):
        try:
            c = [[0]*len(b[0]) for i in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b[0])):
                    c[i][j] = self.add_1(a[i],[t[j] for t in b])
            return c
        except:
            print('a和b形状不匹配')
        
    def divide(self,a,b):
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c = copy.deepcopy(a)
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] /= b[i][j]
            return c
        else:
            c = self.expend(a)
            d = self.expend(b)
            try:
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        c[i][j] /= d[i][j]
                return c
            except:
                print('a和b形状不匹配')
        
    def transpose(self,a):
        c = [[0]*len(a) for i in range(len(a[0]))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[j][i] = a[i][j]
        return c 


if __name__ == '__main__':

    m,n = list(map(int,input().split()))
    mat_a = []
    for i in range(m):
        mat_a.append(list(map(int,input().split())))
    m,n = list(map(int,input().split()))
    mat_b = []
    for i in range(m):
        mat_b.append(list(map(int,input().split())))

    fun1 = use_numpy()
    fun2 = without_numpy()
            # print('input:')
            # print('mat_a:')
            # print_list(mat_a)
            # print('mat_b:')
            # print_list(mat_b)
            # print('use_numpy:')
            # print('add = ')
            # print_list(fun1.add(mat_a,mat_b))
            # print('sub = ')
            # print_list(fun1.sub(mat_a,mat_b))
            # print('mul = ')
            # print_list(fun1.mul(mat_a,mat_b))
            # print('divide = ')
            # print_list(fun1.divide(mat_a,mat_b))
            # print('transpose = ')
            # print_list(fun1.transpose(mat_a))


            # print('without_numpy:')
            # print('add = ')
            # print_list(fun2.add(mat_a,mat_b))
            # print('sub = ')
            # print_list(fun2.sub(mat_a,mat_b))
            # print('mul = ')
            # print_list(fun2.mul(mat_a,mat_b))
            # print('divide = ')
            # print_list(fun2.divide(mat_a,mat_b))
            # print('transpose = ')
            # print_list(fun2.transpose(mat_a))   
                    
    print('use_numpy:')
    s = time()
    for i in range(1000):
        fun1.add(mat_a,mat_b)
    print('add_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun1.sub(mat_a,mat_b)
    print('sub_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun1.mul(mat_a,mat_b)
    print('mul_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun1.divide(mat_a,mat_b)
    print('divide_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun1.transpose(mat_a)
    print('transpose_time = ',time()-s)



    print('without_numpy:')
    s = time()
    for i in range(1000):
        fun2.add(mat_a,mat_b)
    print('add_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun2.sub(mat_a,mat_b)
    print('sub_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun2.mul(mat_a,mat_b)
    print('mul_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun2.divide(mat_a,mat_b)
    print('divide_time = ',time()-s)
    s = time()
    for i in range(1000):
        fun2.transpose(mat_a)
    print('transpose_time = ',time()-s)