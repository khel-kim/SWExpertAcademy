T = int(input())
data = []
for _ in range(T):
    v, e = list(map(int, input().split()))
    edges = []
    for __ in range(e):
        edges.append(list(map(int, input().split())))
    question = list(map(int, input().split()))
    data.append((v, e, edges, question))


def make_edge_dict(v, edges):
    dic = {}
    for i in range(v):
        dic[i] = []
    for i, j in edges:
        dic[i-1].append(j-1)
    return dic


def sol(case):
    v = case[0]
    # e = case[1]
    edges = case[2]
    question = case[3]

    edge_dic = make_edge_dict(v, edges)
    start = question[0] - 1
    end = question[1] - 1

    visit = [start]
    stack = [start]
    while stack:
        current = stack[-1]
        len_visit = len(visit)
        # visit.append(current)
        # print(stack, visit)
        for i in edge_dic[current]:
            if i not in visit:
                stack.append(i)
                visit.append(i)
                break
        if len_visit == len(visit):
            stack.pop(-1)

    if end in visit:
        return 1
    else:
        return 0


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
