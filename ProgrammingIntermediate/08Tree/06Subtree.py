class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def pre_order_traverse(top):
    global visit
    if top:
        # print(top.data)
        visit.append(top.data)
        pre_order_traverse(top.left)
        pre_order_traverse(top.right)


def sol(case):
    global visit
    e, n, edges = case
    n_nodes = max(edges)
    nodes = [Node(i + 1) for i in range(n_nodes)]
    for i in range(0, len(edges), 2):
        parent_index = edges[i] - 1
        child_index = edges[i + 1] - 1
        if nodes[parent_index].left is None:
            nodes[parent_index].left = nodes[child_index]
        else:
            nodes[parent_index].right = nodes[child_index]
    visit = []
    pre_order_traverse(nodes[n - 1])
    # print(visit)
    return len(visit)


T = int(input())
data = []
for _ in range(T):
    e, n = list(map(int, input().split()))
    edges = list(map(int, input().split()))
    data.append((e, n, edges))
for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))