board = [i for i in range(1, 13)]
T = int(input())
data = []
for _ in range(T):
    n, k = list(map(int, input().split()))
    data.append((n, k))

################## sol1
def sol1(arr, board):
    n = arr[0]
    k = arr[1]
    count = 0
    for i in range(1 << 12):
        candi = []
        if bin(i).count('1') != n: continue
        for j in range(len(board)):
            if i & (1 << j):
                candi.append(board[j])
        if len(candi) == n and sum(candi) == k:
            count +=1
    return count

for i, arr in enumerate(data):
    print("#%s" %(i + 1), sol1(arr, board))

################ sol2
def combination(arr, m):
    visit = []
    def generator(arr, m, i=0):
        if len(visit) == m:
            yield visit
        else:
            for j in range(i, len(arr)):
                if arr[j] in visit: continue
                visit.append(arr[j])
                yield from generator(arr, m, i=j+1)
                visit.pop()
    yield from generator(arr, m)

def sol2(arr, baord):
    n = arr[0]
    k = arr[1]
    count = 0
    for candi in combination(board, n):
        if sum(candi) == k:
            count += 1
    return count

for i, arr in enumerate(data):
    print("#%s" %(i + 1), sol2(arr, board))