T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, input().split())))


def sol(case):
    n, a, b = case
    k = min(a, b)

    B = [[1]]
    for i in range(1, n+1):
        B.append([])
        for j in range(min([k+1, i+1])):
            # print(i, j, B)
            if j == 0 or j == i:
                B[-1].append(1)
            else:
                B[-1].append(B[-2][j] + B[-2][j-1])
    # print(B)
    return B[-1][-1]


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
