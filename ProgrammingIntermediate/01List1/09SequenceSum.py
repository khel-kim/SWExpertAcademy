T = int(input())
data = []
for i in range(T):
    n, m = list(map(int, input().split()))
    sequence = tuple(map(int, input().split()))
    data.append((n, m, sequence))
##############################################################


def sol(arr):
    n, m, sequence = arr
    candi = []
    for i in range(len(sequence[:-m + 1])):
        candi.append(sum(sequence[i:i + m]))
    return max(candi) - min(candi)


for i, arr in enumerate(data):
    print("#%s" %(i + 1), sol(arr))
