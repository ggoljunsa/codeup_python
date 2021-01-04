n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(n):
    for j in range(i+1, n):
        if abs(l[i] - l[j]) % m == 0:
            print("no")
            exit(1)
            
print("yes")