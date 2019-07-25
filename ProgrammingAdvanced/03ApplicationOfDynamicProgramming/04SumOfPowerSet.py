T = int(input())
data = []
for _ in range(T):
    tmp = list(map(int, input().split()))
    data.append(tmp)


def sol(case):
    n, k = case
    R = []
    for _ in range(n + 1):
        R.append([0] * (k + 1))

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            check = j - i
            R[i][j] += R[i - 1][j]
            if check < 0: continue
            elif check == 0:
                R[i][j] += 1
                continue
            elif check > 0:
                R[i][j] += R[i - 1][check]
                continue
    return R[-1][-1]


for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))
