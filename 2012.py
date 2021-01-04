a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    s = str(i)
    
    for j in range(len(s)):
        if s[j] == '1':
            cnt +=1

print(cnt)