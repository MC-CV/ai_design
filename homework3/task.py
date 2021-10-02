

def quicksort(l1,l,r):
    if l<r:
        i = l
        j = r
        temp = l
        while i<j:
            while i<j and l1[temp] <= l1[j]:
                j -= 1
            while i<j and l1[temp] >= l1[i]:
                i += 1
            l1[i],l1[j] = l1[j],l1[i]
        l1[j],l1[temp] = l1[temp],l1[j]
        quicksort(l1,l,i-1)
        quicksort(l1,i+1,r)


class mergesort:
    def __init__(self,arr):
        temp = [0]*len(arr)
        self.sort(arr,0,len(arr)-1,temp)
    def sort(self,arr,l,r,temp):
        if l<r:
            mid = (l+r)//2
            self.sort(arr,l,mid,temp)
            self.sort(arr,mid+1,r,temp)
            self.merge(arr,l,mid,r,temp)

    def merge(self,arr,l,mid,r,temp):
        i = l
        j = mid+1
        t = 0
        while i<=mid and j<=r:
            if arr[i]<=arr[j]:
                temp[t] = arr[i]
                t += 1 
                i += 1
            else:
                temp[t] = arr[j]
                t += 1
                j += 1
        while i<=mid:
            temp[t] = arr[i]
            t += 1
            i += 1
        while j<=r:
            temp[t] = arr[j]
            t += 1
            j += 1
        t = 0

        while l<=r:
            arr[l] = temp[t]
            l += 1
            t += 1


def bumblesort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-i-1):
            if l1[j] > l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]

def insertsort(l1):
    for i in range(1,len(l1)):
        j = i
        while j>0:
            if l1[j] < l1[j-1]:
                l1[j],l1[j-1] = l1[j-1],l1[j]
                j -= 1
            else:
                break


if __name__ == '__main__':
    while True:
        try:
            s = input().split()
            l1 = [int(i) for i in s]
            print('origin:',l1)
            a = l1.copy()
            b = l1.copy()
            c = l1.copy()
            d = l1.copy()
            # quicksort
            quicksort(a,0,len(a)-1)
            print('quicksort:',a)
            # mergesort
            s2 = mergesort(b)
            print('mergesort',b)
            # bumblesort
            bumblesort(c)
            print('bumblesort:',c)
            # insertsort
            insertsort(c)
            print('insertsort:',c)
        except:
            break