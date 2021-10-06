import re
while True:
    try:
        s = input()
        pa = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
        print(pa.search(s))
    except:
        break