T = int(input())
data =[]
for _ in range(T):
    n, m = list(map(int, input().split()))
    case = list(map(int, input().split()))
    data.append((n, m, case))

# case = (3, 10, [5527, 731, 31274])


def sol(case):
    n = case[0]
    m = case[1]
    array = case[2]
    for _ in range(m):
        tmp = array.pop(0)
        array.append(tmp)
    return array[0]


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))