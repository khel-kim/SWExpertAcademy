T = int(input())
data = []
for _ in range(T):
    tmp = list(map(int, input().split()))
    data.append(tmp)


def lis_dp(lis, case):
    for i in range(1, len(case)):
        lis[i] = 1
        for j in range(1, i):
            if case[j] < case[i] and 1 + lis[j] > lis[i]:
                lis[i] = 1 + lis[j]
    return max(lis)


def sol(case):
    lis = [0] * (len(case) + 1)
    return lis_dp(lis, case)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
