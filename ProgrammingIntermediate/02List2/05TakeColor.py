T = int(input())
data = []
for _ in range(T):
    n = int(input())
    color = []
    for __ in range(n):
        color.append(list(map(int, input().split())))
    data.append(color)


def sol(color):
    count = 0
    for arr in color:
        x1, y1, x2, y2, kind = arr
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += 1
                if board[i][j] == 2:
                    count += 1
    return count


for i, color in enumerate(data):
    board = [[0 for _ in range(10)] for _ in range(10)]
    print("#%s" %(i+1), sol(color))
