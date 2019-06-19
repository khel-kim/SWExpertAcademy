T = int(input())
data = []
for _ in range(T):
    data.append(float(input()))


def sol(case):
    if case == 0:
        return 0
    digit = []
    n = 1
    while True:
        if n > 12:
            break
        if case >= (1/2) ** (n):
            digit.append("1")
            case -= (1/2) ** (n)
        else:
            digit.append("0")
        if not case:
            break
        n += 1
    if case:
        return "overflow"
    else:
        return "".join(digit)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
