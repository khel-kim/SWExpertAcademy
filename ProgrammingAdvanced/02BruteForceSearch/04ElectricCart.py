import itertools


def perm2(n, k=0):
    global arr
    if k == n:
        yield [0] + arr + [0]
    else:
        for j in range(k, n):
            arr[j], arr[k] = arr[k], arr[j]
            yield from perm2(n, k=k+1)
            arr[j], arr[k] = arr[k], arr[j]


def perm():
    global visit
    if len(visit) == n:
        yield visit + [0]
    else:
        for j in range(1, n):
            if j in visit: continue
            visit.append(j)
            yield from perm()
            visit.pop()


def sol(case):
    global visit, n
    n, board = case
    visit = [0]
    sums = []
    for route in itertools.permutations([i for i in range(1, n)]):
        route = [0] + list(route) + [0]
        sum = 0
        for i in range(len(route) - 1):
            sum += board[route[i]][route[i + 1]]
        sums.append(sum)
    return min(sums)


T = int(input())
data = []
for _ in range(T):
    n = int(input())
    board = []
    for __ in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
    data.append((n, board))

for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
