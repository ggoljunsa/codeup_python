st = input()
cnt = 0
s = len(st)-1
for i in range(s+1):
    temp = ord(st[i])
    cnt += (temp - 64) * (26 ** (s-i))

print(cnt)