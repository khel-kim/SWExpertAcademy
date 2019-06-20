def get_route(moves, length, n, board):
    global visit, summation
    if len(visit) == length:
        # print(visit, summation)
        yield summation
    else:
        x, y = visit[-1]
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visit: continue
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            visit.append((nx, ny))
            summation += board[nx][ny]
            yield from get_route(moves, length, n, board)
            visit.pop()
            summation -= board[nx][ny]


def sol(case):
    global visit, summation
    n, board = case
    moves = ((1, 0), (0, 1))
    length = 2 * n - 1
    visit = [(0, 0)]
    summation = board[0][0]
    sums = []
    for sum in get_route(moves, length, n, board):
        sums.append(sum)
    # print(sums)
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
    print("#%s" % (i + 1),sol(case))