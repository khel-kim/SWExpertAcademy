T = int(input())
data = []
for _ in range(T):
    data.append(int(input()))


def sol(case):
    # print(case)
    n = case - 1
    memo = [1, 3, 6]

    if n == 0 or n == 1 or n == 2:
        return memo[n]
    else:
        for i in range(3, n+1):
            memo.append(memo[i-1] + memo[i-2] * 2 + memo[i-3])
            # print(memo)
        return memo[-1]


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))