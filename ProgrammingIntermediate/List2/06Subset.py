board = [i for i in range(1, 13)]
T = int(input())
data = []
for _ in range(T):
    n, k = list(map(int, input().split()))
    data.append((n, k))

arr = data[2]
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
        print(candi)
        if len(candi) == n and sum(candi) == k:
            count +=1
    return count

for i, arr in enumerate(data):
    print("#%s" %(i + 1), sol1(arr, board))
