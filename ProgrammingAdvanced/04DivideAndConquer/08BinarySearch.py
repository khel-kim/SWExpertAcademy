def binary_search(number, a):
    if len(a) == 1:
        if a[0] == number:
            return 1
        else:
            return 0
    elif len(a) == 0:
        return 0
    n = len(a)
    middle = n // 2
    if a[middle] == number:
        return 1
    elif a[middle] >= number:
        return binary_search(number, a[:middle])
    elif a[middle] <= number:
        return binary_search(number, a[middle + 1:])


T = int(input())
data = []
for _ in range(T):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    data.append((n, m, a, b))

for i, case in enumerate(data):
    n, m, a, b = case
    count = 0
    for j in b:
        count += binary_search(j, a)
    print("#%s" % (i + 1), count)
