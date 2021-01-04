n, k = map(int, input().split())
cnt = ['0', '1', '2', '3', '4', '5', '6', 
'7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

m = []
if n == 0:
    print(0)
    exit(1)
    
while n>0:
    m.append((int(n%k)))
    n= int(n/k)

for i in range(len(m)-1, -1, -1):
    print(cnt[m[i]], end = '')
