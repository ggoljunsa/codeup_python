K = int(input())
code = list(input())
l = []
for i in range(len(code)):
    new = ord(code[i]) - 3*(i+1) - K
    while(1):
        if new >= 65:
             break
        else:
            new += 26
    print(chr(new), end = '')