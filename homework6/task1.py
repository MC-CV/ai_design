import pandas as pd
import numpy as np
import os

rootpath = 'dataset'
# files = ['yob2011.txt','yob2012.txt']
files = []
for i,j,k in os.walk(rootpath):
    for file in k: 
        if file.endswith('.txt'):
            files.append(file)
# 统计男女人数
def task1():
    table = pd.DataFrame(columns=['times'],index=['M','F'])
    table['times']['M'] = 0
    table['times']['F'] = 0
    for name in files:
        path = os.path.join(rootpath+'/'+name)
        with open(path,'r') as temp:
            for i in temp.readlines():
                s = i.strip().split(',')
                table['times'][s[1]] += int(s[2])
        print(name,'finished.')
    print(table)

def task1_ex():
    table = pd.DataFrame(columns=['times'],index=['M','F'])
    table['times']['M'] = 0
    table['times']['F'] = 0
    d1 = {}
    d1['M'] = []
    d1['F'] = []
    for name in files:
        path = os.path.join(rootpath+'/'+name)
        with open(path,'r') as temp:
            for i in temp.readlines():
                s = i.strip().split(',')
                if d1[s[1]].__contains__(s[0]):
                    continue
                else:
                    d1[s[1]].append(s[0])
                    table['times'][s[1]] += 1
        print(name,'finished.')
    print(table)

def task2():
    names = {}
    for name in files:
        path = os.path.join(rootpath+'/'+name)
        with open(path,'r') as temp:
            for i in temp.readlines():
                s = i.strip().split(',')
                try:
                    names[s[0]] += int(s[2])
                except:
                    names[s[0]] = int(s[2])
        print(name,'finished.')
    res = pd.DataFrame(names.values(),columns=['names'],index=names.keys())
    print(res.iloc[:5])

def task3():
    names = {}
    for name in files:
        path = os.path.join(rootpath+'/'+name)
        with open(path,'r') as temp:
            for i in temp.readlines():
                s = i.strip().split(',')
                try:
                    names[s[0]] += int(s[2])
                except:
                    names[s[0]] = int(s[2])
        print(name,'finished.')
    res = pd.DataFrame(names.values(),columns=['names'],index=names.keys())
    res = res.sort_values('names',ascending = False)
    print(res.iloc[:5])

def task4():
    names = {}
    for name in files:
        path = os.path.join(rootpath+'/'+name)
        with open(path,'r') as temp:
            for i in temp.readlines():
                s = i.strip().split(',')
                try:
                    names[s[0]] += int(s[2])
                except:
                    names[s[0]] = int(s[2])
        print(name,'finished.')
    res = pd.DataFrame(names.values(),columns=['names'],index=names.keys())
    print('共出现',len(res),'个名字')

if __name__ == '__main__':
    # task1()
    task1_ex()
    # task2()
    # task3()
    # task4()

