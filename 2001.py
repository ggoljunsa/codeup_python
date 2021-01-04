pasta = [0 for _ in range(3)]
juice = [0 for _ in range(2)]
pasta_min = 2000
juice_min = 2000

for i in range(3):
    pasta[i] = int(input())
    if pasta[i] < pasta_min:
        pasta_min = pasta[i]

for i in range(2):
    juice[i] = int(input())
    if juice[i] < juice_min:
        juice_min = juice[i]

result = (juice_min+pasta_min)*1.1
print('%.1f' % result)