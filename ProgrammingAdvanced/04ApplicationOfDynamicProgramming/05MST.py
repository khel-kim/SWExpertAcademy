from pprint import pprint

T = int(input())
inf = 10 ** 5
data = []
for _ in range(T):
    n = int(input())
    board = []
    for __ in range(n):
        board.append([])
        for i in map(int, input().split()):
            if i == 0: board[-1].append(inf)
            else: board[-1].append(i)
    data.append(board)

# pprint(data)
# case = data[1]
# pprint(case)


def sol(case):
    n = len(case)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            for k in range(n):
                if k == i or k == j: continue
                if case[j][k] > case[j][i] + case[i][k]:
                    case[j][k] = case[j][i] + case[i][k]
    # pprint(case)
    max_num = 0
    for i in range(n):
        for j in range(n):
            if max_num < case[i][j] < inf:
                max_num = case[i][j]
    return max_num


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
