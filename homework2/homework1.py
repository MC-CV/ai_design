while True:
    try:
        l1 = []
        s = input().strip('[').strip(']').split(',')
        for i in s:
            l1.append(int(i))
        # 使用双指针的方法，时间复杂度为O(n)
        l = 0
        r = len(l1)-1
        s = (r-l)*min(l1[l],l1[r])
        while l<r:
            if l1[l]<l1[r]:
                l += 1
            else:
                r -= 1
            s = max(s,min(l1[l],l1[r])*(r-l))
        print("最大的容量为",s)
        l = 0
        r = len(l1)-1
        temp = (r-l)*min(l1[l],l1[r])
        while l<r:
            if l1[l]<l1[r]:
                l += 1
            else:
                r -= 1
            temp = max(s,min(l1[l],l1[r])*(r-l))
            if temp == s:
                print("选择第",l+1,"根和第",r+1,"根线")
                break
    except:
        break