count = 0
a = int(input())
cnt = 0
temp = a
b = []
while a > 0:
    b.append(int(a % 10))
    a /= 10
    a = int(a)
    cnt += 1


for i in range(cnt):
    if b[i] % 3 == 0 and b[i] > 0:
        count += 1
if count == 0:
    print(temp)
else:
    for i in range(count):
        print("K", end="")
