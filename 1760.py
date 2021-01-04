l = list(input())
code = input()

for i in range(len(code)):
    if code[i] == ' ':
        print(' ', end='')
    else:
        for j in range(10):
            if code[i] == l[j]:
                print(j, end='')
                break
