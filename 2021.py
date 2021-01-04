N = int(input())
l = [0 for _ in range(1001)]


max = -1
for i in range(N):
    temp = int(input())
    if temp > max:
        max = temp
    l[temp] += 1
f_num = -1
f_max = -1
s_num = -1
s_max = -1

for i in range(1, max+1):
    if l[i] > f_max:
        f_num = i
        f_max = l[i]

chai = -1

for i in range(max, 0, -1):
    if i != f_num and l[i] >= s_max:
        if abs(i - f_num) > chai:
            s_num = i
            s_max = l[i]
            chai = abs(s_num - f_num)


print(chai)