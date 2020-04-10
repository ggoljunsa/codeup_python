n = int(input())
m = []

allcorrect = True


def debug(num):
    global allcorrect
    correctFlag = True
    inflag = False
    oriMin = m[3]
    realMin = 100100000
    for i in range(3):
        if m[i] == oriMin:
            inflag = True
        elif m[i] < realMin:
            realMin = m[i]
    if realMin < oriMin:
        correctFlag = False

    if inflag and correctFlag:
        pass
    else:
        print(num + 1, realMin)
        allcorrect = False


for i in range(n):
    m = input().split()
    m = list(map(int, m))
    debug(i)
    m.clear()

if allcorrect:
    print(-1)
