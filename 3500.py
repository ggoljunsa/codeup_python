import sys
sys.setrecursionlimit(500000)

l = []

pos = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]


memo = [[-2 for _ in range(11)] for _ in range(11)]
sch = [[0 for _ in range(11)] for _ in range(11)]

def mines(y, x):
    cnt = 0
    for i in range(8):
        temp_r = y + pos[i][0]
        temp_c = x + pos[i][1]
        if temp_r >=0 and temp_r<9 and temp_c>=0 and temp_c<9:
            cnt += l[temp_r][temp_c]
    return cnt

def f(y, x):
    global memo
    global sch
    if y<0 or x<0 or y>8 or x>8:#1. position is out of range
        return
    if sch[y][x] ==1: #2. already searched
        return
    if l[y][x] !=0: #3.if mine exsists in first position
        memo[y][x] = -1
        return
    mine = mines(y, x)
    memo[y][x] = mine
    sch[y][x] = 1
    #4.if belonging mine amount 0+unsearched land is 0, searches again
    if mine == 0:
        for i in range(8):
            f(y+pos[i][0], x+pos[i][1])
    else:
        return

def prt():
    for i in range(9):
        for j in range(9):
            if memo[i][j] == -2:
                print("_ ", end = '')
            else:
                print("%d " %memo[i][j], end = '')
        print()

for i in range(9):
    l.append(list(map(int, input().split())))
r, c = map(int, input().split())
r-=1
c-=1
f(r, c)
prt()
