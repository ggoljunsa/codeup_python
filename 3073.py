

n, m = map(int, input().split())
l = []
memo = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(0, n):
    for j in range(0, m):
        if i<1 and j<1:
            memo[i][j] = l[i][j]
        elif j<1 and i>=1:
            memo[i][j] = memo[i-1][j] + l[i][j]
        elif j>=1 and i<1:
            memo[i][j] = memo[i][j-1] + l[i][j]
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1]) + l[i][j]

print(memo[n-1][m-1])