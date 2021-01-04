a, b = map(int, input().split())

def ks(x):
    l = str(x)
    cnt = 0
    for i in range(len(l)):
        if l[i] == '3' or l[i] == '6' or l[i] == '9':
            cnt += 1
    return cnt

for i in range(a, b+1):
    amount = ks(i)
    if amount == 0:
        print(i)
    else:
        for _ in range(amount):
            print('K', end = '')
        print()