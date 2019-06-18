T = int(input())
data = []
for _ in range(T):
    n, m, l = list(map(int, input().split()))
    leaf_node = []
    for __ in range(m):
        leaf_node.append(list(map(int, input().split())))
    data.append((n, m, l, leaf_node))


def sol(case):
    n, m, l, leaf_node = case
    last_index = sorted(leaf_node)[-1][0]
    heap = [-1 for _ in range(last_index + 1)]

    for index, number in leaf_node:
        heap[index] = number

    if last_index % 2 == 1:
        for i in range(last_index, 1, -2):
            heap[i // 2] = heap[i] + heap[i - 1]
    if last_index % 2 == 0:
        heap[last_index // 2] = heap[last_index]
        for i in range(last_index - 1, 1, -2):
            heap[i // 2] = heap[i] + heap[i - 1]
    return heap[l]


for i, case in enumerate(data):
    print("#%s" % (i + 1),sol(case))