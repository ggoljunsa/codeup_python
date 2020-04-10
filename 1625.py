n = int(input())
temp = 0
cycleFlag = False
m = []
for i in range(n):
    k = int(input())
    while cycleFlag == False:
        temp += k % 10
        k /= 10
        k = int(k)
        if k == 0:
            cycleFlag = True
        if cycleFlag:
            if temp != 0 and temp >= 10:
                k = temp
                temp = 0
                cycleFlag = False
            elif temp < 10:
                m.append(temp)
                temp = 0
    cycleFlag = False

for i in range(n):
    print(m[i])
