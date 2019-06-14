T = int(input())
data = []
for _ in range(T):
    v, e = list(map(int, input().split()))
    edges = []
    for __ in range(e):
        node1, node2 = list(map(int, input().split()))
        edges.append([node1, node2])
    start, end = list(map(int, input().split()))
    data.append((v, e, edges, start, end))


def get_edge_dic(dic, edges):
    for i, j in edges:
        dic[i].append(j)
        dic[j].append(i)


def sol(case):
    v = case[0]
    e = case[1]
    edges = case[2]
    start = case[3]
    end = case[4]

    if start == end:
        return 0

    dic = {}
    for i in range(v):
        dic[i + 1] = []

    get_edge_dic(dic, edges)

    queue = [start]
    visit = [start]
    last = None
    check = False
    count = 1
    while queue:
        # print(queue)
        current = queue.pop(0)
        candi = dic[current]

        for i in candi:
            if i in visit: continue
            if i == end:
                check = True
                break
            queue.append(i)
            visit.append(i)

        if check:
            break

        if count == 1:
            count += 1
            last = visit[-1]
        else:
            if last == current:
                last = visit[-1]
                count += 1
    return count


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))