from pprint import pprint
T = int(input())
data = []
for _ in range(T):
    n = int(input())
    for __ in range(n):
        board = []
        tmp = input().split()
        for number in tmp:
            if number == "0":
                board.append(100000)
            else:
                board.append(int(number))
        data.append(board)

pprint(data)
case = data[0]

# sol













# test case
# 3
# 3
# 0 18 34
# 48 0 55
# 18 7 0
# 4
# 0 83 65 97
# 82 0 78 6
# 19 19 0 82
# 6 34 94 0
# 5
# 0 9 26 85 42
# 14 0 84 31 27
# 58 88 0 16 46
# 83 61 94 0 17
# 40 71 24 38 0

# result
# 1 89
# 2 96
# 3 139