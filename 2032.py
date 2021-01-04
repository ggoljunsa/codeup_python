st = input()

num = int(st) / (10 **len(st))

l = ''
while len(l) < 10:
    num *=2
    if int(num)>=1:
        l +='1'
        num -=1
    else:
        l +='0'

print(l)