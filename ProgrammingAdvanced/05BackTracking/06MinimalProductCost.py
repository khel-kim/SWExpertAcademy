T = int(input())
data = []
for _ in range(T):
    board = []
    n = int(input())
    for __ in range(n):
        line = list(map(int, input().split()))
        board.append(line)
    data.append((n, board))


def back_tracking():
    global best
    if len(visit) == n:
        cost = 0
        for i, j in enumerate(visit):
            cost += board[i][j]
        if best > cost:
            best = cost
        # print(best, visit)
    else:
        for factory in range(n-1, -1, -1):
            if check[factory]: continue
            visit.append(factory)
            check[factory] = True

            cost = 0
            for i, j in enumerate(visit):
                cost += board[i][j]
            if best < cost:
                visit.pop()
                check[factory] = False
                continue

            back_tracking()
            visit.pop()
            check[factory] = False


def sol(case):
    global check, visit, best, n, board
    n, board = case
    check = [False] * n
    visit = []
    best = 100000
    back_tracking()
    return best


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
