T = int(input())
data = []
for _ in range(T):
    n, m = list(map(int, input().split()))
    stuff = []
    for __ in range(m):
        s, p = list(map(int, input().split()))
        stuff.append((s, p))
    data.append((n, stuff))


def knapsack():
    for i in range(1, len(stuff) + 1):
        for j in range(1, n + 1):
            if stuff[i-1][0] > j:
                W[i][j] = W[i-1][j]
            else:
                W[i][j] = max(W[i-1][j - stuff[i-1][0]] + stuff[i-1][1], W[i-1][j])
    return W[-1][-1]


def sol(case):
    global W, n, stuff
    n, stuff = case[0], case[1]
    W = []
    for _ in range(len(stuff) + 1):
        W.append([0] * (n + 1))
    return knapsack()


for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))

