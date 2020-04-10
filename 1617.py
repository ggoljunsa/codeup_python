x = int(input())
list_rev = []
z = x
y = 0
while x != 0:
    list_rev.append(x % 10)
    x /= 10
    x = int(x)
len = len(list_rev)
for i in range(len):
    y += list_rev[i] * pow(10, len - i - 1)


p = z + y
tot = p
list_tot = []
len = 0

while tot != 0:
    list_tot.append(tot % 10)
    tot /= 10
    tot = int(tot)
    len += 1


flag = True


i = 0
j = len - 1

while i < j:
    if list_tot[i] != list_tot[j]:
        flag = False
    i += 1
    j -= 1


if flag:
    print("YES")
else:
    print("NO")
