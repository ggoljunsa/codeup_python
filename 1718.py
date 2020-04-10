y = input()
x = list(y)
len = len(x)
c = 0
h = 0

molecule = [0, 0]

num = 0
for i in range(len):
    if x[i] == "C":
        if i == len - 1:
            c += 1
        elif i < len - 1:
            if x[i + 1] == "H":
                c += 1
            elif x[i + 1].isdecimal() == True:
                num = i + 1
                while x[num].isdecimal() == True:
                    c *= 10
                    c += int(x[num])
                    num += 1
                    if num > (len - 1):
                        break
        molecule[0] += c
        c = 0

    elif x[i] == "H":
        if i == len - 1:
            h += 1
        if i < len - 1:
            if x[i + 1] == "C":
                h += 1
            elif x[i + 1].isdecimal() == True:
                num = i + 1
                while x[num].isdecimal() == True:
                    h *= 10
                    h += int(x[num])
                    num += 1
                    if num > (len - 1):
                        break
        molecule[1] += h
        h = 0


total = molecule[0] * 12 + molecule[1] * 1
print(molecule)
print(total)
