T = int(input())
data = []
for i in range(T):
    n, m = list(map(int, input().split()))
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    data.append((n, m, W, T))


def sol(case):
    n, m, W, T = case

    sorted_W = sorted(W, reverse=True)
    sorted_T = sorted(T, reverse=True)

    result = 0
    while sorted_W and sorted_T:
        current = sorted_W.pop(0)
        if current <= sorted_T[0]:
            sorted_T.pop(0)
            result += current
            continue
        else:
            continue
    return result


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
