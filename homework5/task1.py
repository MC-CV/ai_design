import matplotlib.pyplot as plt
from wordcloud import WordCloud
d1 = {}
if __name__ == '__main__':
    with open('target.txt','r',encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip().split()
            for j in s:
                try:
                    if 33<=ord(j)<=47:
                        continue
                except:
                    try:
                        if d1[j] != None:
                            d1[j] += 1
                    except:
                        d1[j] = 1
    with open('results.txt','w',encoding='utf-8') as f1:
        l1 = sorted(d1.items(),key=lambda x:x[1],reverse=True)
        for key,value in l1:
            f1.write(key)
            f1.write(':')
            f1.write(str(value))
            f1.write('\n')

    wc = WordCloud(
        background_color="white",
        font_path='123.ttf',
        max_words=100,  
        max_font_size=1000 
        )
    wc.generate_from_frequencies(d1)  
    plt.imshow(wc)
    plt.axis("off")  
    plt.show()
    wc.to_file('词云.png') 

