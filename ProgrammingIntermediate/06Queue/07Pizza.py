T = int(input())
data = []
for _ in range(T):
    n, m = list(map(int, input().split()))
    case = list(map(int, input().split()))
    data.append((n, m, case))

###############


def sol(case):
    n = case[0]
    m = case[1]
    pizza = case[2]
    pizza_index = []
    for i, cheese in enumerate(pizza):
        pizza_index.append([i, cheese])
    queue = [pizza_index.pop(0)]
    count = 1
    while queue:
        # print(queue)
        # init
        if count < n:
            try:
                queue.append(pizza_index.pop(0))
            except IndexError:
                pass
            count += 1
            continue
        cheese = queue.pop(0)
        if cheese[1] // 2 == 0:
            finish = cheese
            try:
                queue.append(pizza_index.pop(0))
            except IndexError:
                pass
        else:
            tmp = [cheese[0], cheese[1]//2]
            queue.append(tmp)
    return finish[0] + 1


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))





