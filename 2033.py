k, n = map(int, input().split())

l = [0 for _ in range(100001)]
r = [0 for _ in range(100001)]

for i in range(n):
    l[i], r[i] = map(int, input().split())
    

start = int(input())

for i in range(n):
    if l[i] == start:
        start = r[i]
    elif r[i] == start:
        start = l[i]

print(start)
