import random
# 使用快速排序,时间复杂度O(nlogn),最差O(n**2)
def quicksort(l1,l,r):
    if l<r: #用于退出递归判断
        i = l 
        j = r
        temp = l1[l] #选择最左边的作为基准
        while i<j:
            while i<j and temp<=l1[j]: #j先从右边往左边搜寻小于基准值的值
                j -= 1
            while i<j and temp>=l1[i]: #接着i从左边往右搜寻大于基准值的值
                i += 1
            l1[i],l1[j] = l1[j],l1[i] #i，j停止后交换两个的位置
        l1[l],l1[i] = l1[i],l1[l] #此时i和j重合，交换基准和此时i的位置，保证基准的左边都比基准小，基准的右边都比基准大
        quicksort(l1,l,i-1) #递归基准左侧
        quicksort(l1,i+1,r) #递归基准右侧
# 使用冒泡排序，时间复杂度O(n**2)
def bumblesort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-i-1): 
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]


def main():
    l1 = []
    l2 = []
    with open('homework1.txt','w') as f:
        for i in range(100): # 生成100个数
            l1.append(random.randint(0,1000))
        for i in l1:
            f.write(str(i)+'\n')
        f.close()
    with open('homework1.txt','r') as f: 
        for line in f.readlines(): # 读取文件中的每一行内容
            l2.append(int(line)) 
        quicksort(l2,0,len(l2)-1)
        # bumblesort(l2)
        with open('homework1_sorted.txt','w') as f1: 
            for i in l2:
                f1.write(str(i)+'\n') # 将内容写入每一行
            f1.close()
        f.close()
if __name__ == '__main__':
    main()