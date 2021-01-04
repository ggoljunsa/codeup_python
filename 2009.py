cup, req = map(int, input().split())

cof = 0
while cup>0:
    if(cup - req <0):
        break
    else:
        cup -= req
        cup += 1
        cof += 1
print(cof)