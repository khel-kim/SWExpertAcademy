from collections import deque
T = int(input())
data = []
for _ in range(T):
    n = int(input())
    start = None
    end = None
    board = []
    for i in range(n):
        board.append([])
        line = input()
        for j in range(n):
            tmp = int(line[j])
            board[i].append(tmp)
            if tmp == 2:
                start = [i, j]
            if tmp == 3:
                end = [i, j]
    data.append((start, end, board))


def sol(case):
    start = case[0]
    end = case[1]
    board = case[2]
    n = len(board)
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    result = False

    queue = deque([start])
    visit = [start]
    count = -1
    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            if board[nx][ny] == 1: continue
            if [nx, ny] in visit: continue
            if board[nx][ny] == 3:
                result = True
                break
            queue.append([nx, ny])
            visit.append([nx, ny])
        if count == -1:
            count += 1
            last = visit[-1]
        else:
            if last == [x, y]:
                count += 1
                # print(count, last, queue)
                last = visit[-1]
    # print(result, count)
    if result:
        return count
    else:
        return 0


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
