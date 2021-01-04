import sys
sys.setrecursionlimit(500000)

n, k = map(int, input().split())
time = [[0, 0] for _ in range(105)]
money = [[0, 0] for _ in range(105)]
temp = []
max_money = 0

def f(t, m, c):
    global max_money
    if t>k:
        return 
    if c == n+1:
        if m > max_money:
            max_money = m
            return
    if time[c-1][0]<time[c-1][1] and money[c-1][0] > money[c-1][1]:
        f(t+time[c-1][0], m+money[c-1][0], c+1)
    elif(time[c-1][0]>time[c-1][1] and money[c-1][0]<money[c-1][1]):
        f(t+time[c-1][1],m+money[c-1][1], c+1)
    else:
        f(t+time[c-1][0],m+money[c-1][0],c+1)
        f(t+time[c-1][1],m+money[c-1][1],c+1)

for i in range(n):
    temp.append(list(map(int, input().split())))
    time[i][0] = temp[i][0]
    money[i][0] = temp[i][1]
    time[i][1] = temp[i][2]
    money[i][1] = temp[i][3]
#print(time, money)
f(0, 0, 1)
print(max_money)

#https://m.blog.naver.com/PostView.nhn?blogId=ckkm0476&logNo=221174255326&proxyReferer=https:%2F%2Fwww.google.com%2F