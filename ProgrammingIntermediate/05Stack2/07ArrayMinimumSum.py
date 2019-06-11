T = int(input())
data = []
for _ in range(T):
    n = int(input())
    board = []
    for __ in range(n):
        board.append(list(map(int, input().split())))
    data.append(board)

case = data[0]
####################
def sol(case):
    visit = []
    candi = [i for i in range(len(case))]
    def permutation(candi):
        if len(visit) == len(case):
            yield visit
        else:
            for j in range(0, len(case)):
                if j in visit: continue
                visit.append(candi[j])
                yield from permutation(candi)
                visit.pop()
    final = []
    for tmp in permutation(candi):
        sum = 0
        for i, j in enumerate(tmp):
            sum += case[j][i]
        final.append(sum)
    return min(final)

for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))