class Node:
    def __init__(self, data, tail=True):
        self.data = data
        self.next = None
        self.prev = None
        self.tail = tail


def append(head, data):
    add_node = Node(data)
    q = head
    while q.tail is not True:
        q = q.next
    q.next = add_node
    add_node.prev = q

    add_node.next = head.next
    q.tail = False
    return head


def insertion(head, step, times):
    linked_list = head
    for _ in range(times):
        for __ in range(step):
            linked_list = linked_list.next
        data = linked_list.data + linked_list.prev.data
        add_node = Node(data, tail=False)
        if linked_list.prev.tail is True:
            add_node.tail = True
            linked_list.prev.tail = False
        add_node.prev = linked_list.prev
        add_node.next = linked_list
        linked_list.prev.next = add_node
        linked_list.prev = add_node

        linked_list = add_node
        # node_checker(head)
    return head


def node_checker(head):
    num = 0
    q = head
    while q:
        print(q.data, q.tail, end=" ")
        q = q.next
        num += 1
        if num > 10:
            break
    print()


def get_list(head):
    tmp_list = []
    q = head
    while q:
        tmp_list.append(q.data)
        if q.tail is True:
            break
        q = q.next
    return tmp_list[::-1]


def sol(case):
    n, m, k, numbers = case[0], case[1], case[2], case[3]
    head = Node(-1)
    for number in numbers:
        head = append(head, number)
    head = head.next
    q = head
    while q.tail is not True:
        q = q.next
    head.prev = q
    head = insertion(head, m, k)
    return get_list(head)


T = int(input())
data = []
for _ in range(T):
    n, m, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    data.append((n, m, k, numbers))

for i, case in enumerate(data):
    print("#%s" % (i + 1), end=" ")
    result = sol(case)
    for j in result[:10]:
        print(j, end=" ")
    print()