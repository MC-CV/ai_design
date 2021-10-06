import re
while True:
    try:
        s = input()
        pa = re.compile(r'\d{6}')
        print('满足要求的为',pa.findall(s),'共',len(pa.findall(s)),'个')
    except:
        break
