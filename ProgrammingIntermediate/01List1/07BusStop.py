T = int(input())
data = []
for _ in range(T):
    k, n, m = map(int, input().split())
    station = tuple(map(int, input().split()))
    data.append((k, n, m, station))


def sol(arr):
    k, n, m, station = arr
    current = 0
    count = 0
    start = 0
    while True:
        now = current
        current += k
        if current >= n:
            return count
        else:
            candi = []
            for i in station[start:]:
                if now + 1 <= i <= current:
                    candi.append(i)
                    start = station.index(i) + 1
                elif current < i:
                    break
        if not candi:
            return 0
        count += 1
        current = candi[-1]


for i, arr in enumerate(data):
    print("#%s" %(i + 1), sol(arr))
