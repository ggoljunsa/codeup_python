x = int(input())
tri = [0, 0, 0]

possibleFlag = False

for i in range(1, int(x / 3) + 1):
    tri[0] = i
    for j in range(i, int((x - i) / 2) + 1):
        tri[1] = j
        tri[2] = x - (tri[1] + tri[0])
        if tri[2] < tri[0] + tri[1]:
            possibleFlag = True
            for i in range(3):
                print(tri[i], end=" ")
            print()

if possibleFlag == False:
    print(-1)
