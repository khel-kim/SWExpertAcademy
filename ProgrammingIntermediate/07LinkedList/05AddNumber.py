T = int(input())
data = []
for _ in range(T):
    n, m, l = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    add_number = []
    for _ in range(m):
        index, number = list(map(int, input().split()))
        add_number.append([index, number])
    data.append((n, m, l, numbers, add_number))

case = data[0]
#################################


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def add_to_last(data):
    global head
    q = head
    while q.next:
        q = q.next
    q.next = Node(data)
    q.next.prev = q


def add(index, data):
    global head
    add_node = Node(data)
    order = -1
    q = head
    while q.next:
        if order == index:
            break
        q = q.next
        order += 1
    q.prev.next = add_node
    add_node.prev = q.prev
    add_node.next = q
    q.prev = add_node


def delete():
    pass


def get(index):
    global head
    q = head
    order = -1
    while q.next:
        if order == index:
            return q.data
        q = q.next
        order += 1

def sol(case):
    global head
    n = case[0]
    m = case[1]
    l = case[2]
    numbers = case[3]
    add_numbers = case[4]
    head = Node(-1)

    while numbers:
        add_to_last(numbers.pop(0))

    while add_numbers:
        index, data = add_numbers.pop(0)
        add(index, data)

    # t = head
    # while t:
    #     print(t.data, "data")
    #     t = t.next

    return get(l)

for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))