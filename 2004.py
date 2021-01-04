a, b = map(int, input().split())
c, d = map(int, input().split())

for i in range(a): #can
    for _ in range(c):
        for j in range(b): #jull
            for _ in range(d): #badukcan
                if (j+i )% 2 == 0:
                    print('X', end = '')
                else:
                    print('.', end = '')
        print()
    