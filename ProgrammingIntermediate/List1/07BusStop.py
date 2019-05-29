T = int(input())
data = []
for _ in range(T):
    k, n, m = map(int, input().split())
    station = tuple(map(int, input().split()))
    data.append((k, n, m, station))
print(data)

def sol(arr):
    k, n, m, station = arr[0], arr[1], arr[2], arr[3]
    current = 0
    count = 0
    while n <= current:
        current += k
