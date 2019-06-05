T = int(input())
data = []
for _ in range(T):
    n, m = list(map(int, input().split()))
    board = []
    for __ in range(n):
        board.append(list(input()))
    data.append([n, m, board])

def search_axis0(n, m, board):
    # print(board)
    for words in board:
        start = 0
        while True:
            check = words[start: start + m]
            # print(check)
            check_reverse = check[::-1]
            if check == check_reverse:
                return check
            else:
                start += 1
                if start + m > n:
                    break
    check = -1
    return check

for i, current in enumerate(data):
    n, m, board = current
    check = search_axis0(n, m, board)
    if check != -1:
        print("#%s" % (i + 1), ''.join(check))
    else:
        board = list(zip(*board))
        check = search_axis0(n, m, board)
        print("#%s" % (i + 1), ''.join(check))