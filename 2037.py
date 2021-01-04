n = int(input())

print('{', end='')

for i in range(n, n*2):
    print('%d' %i, end='')
    if i<(n*2-1):
        print(', ', end='')
print('}')