n = int(input())
cnt = 0

def bad(l):
    if len(l) <= 3:
        return True
    elif l.find('tap') > -1:
        return True
    elif l.find('xocure') > -1:
        return True
    else:
        return False

for i in range(n):
    st = str(input())
    if bad(st):
        cnt+=1
        print(st)

if cnt<=3:
    print('safe')
elif cnt <=6:
    print('warning')
else:
    print('danger')