m=[]
for i  in range(20):
    m.append([])
    for j in range(20):
        m[i].append(0)
n = int(input())
for i in range(n):
    x, y = input().split()
    m[int(x)][int(y)] = 1
for i in range(1, 20):
    for j in range(1, 20):
        print(m[i][j], end = ' ')
    print()