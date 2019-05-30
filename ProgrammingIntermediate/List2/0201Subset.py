arr = [-7, -3, -2, 5, 8]


def sol(arr):
    n = len(arr)
    for i in range(1, 1 << n):
        check = []
        for j in range(n):
            if i & (1 << j):
                check.append(j)
        sum = 0
        for i in check:
            sum += arr[i]
        if sum == 0:
            bool = True
            break
    return bool

