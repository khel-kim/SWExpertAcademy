T = int(input())
data = []
for _ in range(T):
    n = int(input())
    board = []
    for k in range(n):
        board.append([])
        line = input()
        print(line)
        for j in line:
            if j in '0123':
                board[k].append(int(j))
    data.append(board)

def backtrack():
    global check
    x, y = visit[-1][0], visit[-1][1]
    # print(visit)
    # print(board[x][y])
    if board[x][y] == 3: # 만약 솔루션이라면
        # print(visit, "final visit")
        check = True
        return
    else:
        for dx, dy in moves: # 후보군
            nx = x + dx
            ny = y + dy
            if not 0 <= nx < n: continue # 유망성 체크
            if not 0 <= ny < n: continue
            if board[nx][ny] == 1: continue
            if [nx, ny] in visit: continue
            visit.append([nx, ny])
            backtrack()
            visit.pop(-1)


def sol(case):
    global check, visit, board, moves
    board = case
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                start = [i, j]
            elif board[i][j] == 3:
                end = [i, j]
    moves = ((0, 1), (1, 0), (-1, 0), (0, -1))
    visit = [start]
    check = False
    backtrack()
    if check:
        return 1
    else:
        return 0


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
