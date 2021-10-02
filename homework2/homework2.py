while True:
    try:
        a = input()
        b = input()
        temp1 = 1
        temp2 = 1
        sum_a = 0
        sum_b = 0
        # 普通循环，时间复杂度O(n)
        for i in range(-1,-1-len(a),-1):
            sum_a = sum_a + temp1*int(a[i])
            temp1 *= 2
        for i in range(-1,-1-len(b),-1):
            sum_b =sum_b + temp2*int(b[i])
            temp2 *= 2
        res = sum_a+sum_b
        ss = []
        while res:
            b = res%2
            res //= 2
            ss.append(b)
        ss = ss[::-1]
        print("和为",end='')
        for i in ss:
            print(str(i),end = '')
    except:
        break