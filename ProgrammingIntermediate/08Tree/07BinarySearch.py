def in_order_traverse(top):
    global index, visit
    try:
        if index[top]:
            in_order_traverse(2 * top)
            # print(index[top])
            visit.append(index[top])
            in_order_traverse(2 * top + 1)
    except IndexError:
        return


def sol(case):
    global index, visit
    n = case
    index = [i for i in range(n + 1)]
    init_tree = [-1 for _ in range(n + 1)]
    visit = []
    in_order_traverse(1)
    # print(visit)
    for i, location in enumerate(visit):
        init_tree[location] = i + 1
    # print(init_tree)
    return init_tree[1], init_tree[n // 2]


T = int(input())
data = []
for _ in range(T):
    data.append(int(input()))

for i, case in enumerate(data):
    result = sol(case)
    print("#%s" % (i + 1), result[0], result[1])


