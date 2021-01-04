a, b = map(int, input().split())

prev = []
prev.append(1)
now = []

def prt(n = []):
    for i in range(len(n)):
        print('%d ' %n[i], end='')
    print('')

for i in range(1, b+1):
    pos = 0
    if i >= a and i <= b:
        prt(prev)
    now = []
    while pos < len(prev):
        prev_num = prev[pos]
        next_num = prev_num
        cnt_num = 1
        while True:
            pos += 1
            if pos >= len(prev):
                break
            next_num = prev[pos]
            if next_num != prev_num:
                break
            else:
                cnt_num+=1
        now.append(prev_num)
        now.append(cnt_num)
    prev = now
    #print(prev, end=',')
    #print(now, end='')