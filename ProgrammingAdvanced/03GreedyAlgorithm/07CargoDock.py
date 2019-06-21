T = int(input())
data = []
for _ in range(T):
    n = int(input())
    t = []
    for __ in range(n):
        t.append(list(map(int, input().split())))
    data.append((n, t))


def sol(case):
    n, t = case
    t_sorted = sorted(t, key=lambda x: x[1])
    result = [[-1, -1]]
    while t_sorted:
        current = t_sorted.pop(0)
        if result[-1][1] <= current[0]:
            result.append(current)
        else:
            continue
    # print(result)
    return len(result) - 1


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
