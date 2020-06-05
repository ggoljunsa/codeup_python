import threading

n, r = input().split()
n = int(n)
r = int(r)


def multiple(a, b):
    temp = 1
    for i in range(a, b + 1):
        temp *= i
    return temp


def comb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    else:
        tot1 = multiple(n - r + 1, n)
        tot2 = multiple(1, r)
        answer = int(tot1 / tot2)
        return answer


if __name__ == "__main__":
    print(comb(n, r))
