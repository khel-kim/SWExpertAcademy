given_num = 6620

def charge(given_num):
    unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    board = [0 for _ in range(8)]
    start = 0
    while given_num:
        given_num -= unit[start]
        if given_num < 0:
            given_num += unit[start]
            start += 1
            continue
        board[start] += 1
    return board

print(charge(given_num))