st = input()
brd = [0 for _ in range(10)]

cnt = 0

for i in range(len(st)):
    if st[i] == '/':
        cnt += 1
    elif cnt < 1:
        num = ord(st[i]) - 48
        brd[num] +=1
    elif cnt>=1:
        num = ord(st[i]) - 48
        brd[num] -=1

gooddayFlag = True

for i in range(10):
    if brd[i] != 0:
        gooddayFlag = False
        break

if gooddayFlag:
    print('yes')
else:
    print('no')