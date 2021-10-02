def main():
    temp = {}
    with open('text.txt','r') as f:
        for line in f.readlines():
            l1 = line.split(' ') # 按照' '切片划分每个单词
            l1[-1] = l1[-1][:-2] # 把每个结尾单词的'\n'和'.'舍去
            for i in l1:
                i = i.strip(',').strip('.').strip(':').strip('\"').strip('?').strip('!') # 将其他标点符号舍去
            for i in l1:
                try:
                    temp[i] += 1
                except: temp[i] = 1
        with open('homework2_results.txt','w') as f1:
            for k,v in sorted(temp.items(), key = lambda kv:(kv[1], kv[0]),reverse=True): # 对字典按照keys值排序
                f1.write(k+':'+str(v)+'\n')
        f1.close()
    f.close()

if __name__ == '__main__':
    main()
            