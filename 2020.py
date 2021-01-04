l = input()
Flag = True
cnt = 0

pos = 0
a1 = int(l[pos])
R = l[pos+1]
a2 = 0
R_ = 'A'

def num(k = 'A'):
    if k == 'I':
        return 1
    elif k == 'V':
        return 5
    elif k == 'X':
        return 10
    elif k == 'L':
        return 50
    elif k == 'C':
        return 100
    elif k == 'D':
        return 500
    elif k == 'M':
        return 1000
    else:
        return 0

def compare(X, X_):
    cp = ['A','I', 'V', 'X', 'L', 'X', 'C', 'D', 'M']
    pos = 0
    _pos = 0
    while True:
        if cp[pos] == X:
            break
        pos +=1
    while True:
        if cp[_pos] == X_:
            break
        _pos += 1
    if pos >= _pos:
        return 1
    else:
        return -1

for pos in range(2, len(l), 2):
        a2 = int(l[pos])
        R_ = l[pos+1]
        cnt += compare(R, R_)*num(R)*a1
        #print(cnt)
        a1 = a2
        R = R_
cnt += num(R)*a1
print(cnt)