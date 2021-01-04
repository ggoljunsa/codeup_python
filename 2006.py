a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

cnt_n = 0
cnt_b = 0

flag = True
temp = 0
i = 0
while i<s :
    if temp >= a or temp <= -b:
        if flag == True:
            flag = False
        elif flag == False:
            flag = True
        temp = 0
    elif flag == True:
        cnt_n +=1
        temp +=1
        i+=1
    elif flag == False:
        cnt_n -=1
        temp -=1
        i+=1
temp = 0
i = 0
flag = True
while i<s :
    if temp >= c or temp <= -d:
        if flag == True:
            flag = False
        elif flag == False:
            flag = True
        temp = 0
    elif flag == True:
        cnt_b +=1
        temp +=1
        i+=1
    elif flag == False:
        cnt_b -=1
        temp -=1
        i+=1

if cnt_n > cnt_b:
    print('Nikky')
elif cnt_b > cnt_n:
    print('Byron')
else:
    print('Tied')