class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def append(head, data):
    add_node = Node(data)
    q = head
    while q.next:
        q = q.next
    q.next = add_node
    add_node.prev = q
    return head


def insertion(head, index, data):
    add_node = Node(data)
    q = head.next
    order = 0
    while q.next:
        if order == index:
            add_node.prev = q.prev
            add_node.next = q
            q.prev.next = add_node
            q.prev = add_node
            return head
        else:
            q = q.next
            order += 1
    q.next = add_node
    add_node.prev = q
    return head


def delete(head, index):
    q = head.next
    order = 0
    while q.next:
        if order == index:
            q.prev.next = q.next
            q.next.prev = q.prev
            return head
        else:
            q = q.next
            order += 1
    q.prev.next = None
    return head


def interchange(head, index, data):
    q = head.next
    order = 0
    add_node = Node(data)
    while q.next:
        if order == index:
            add_node.prev = q.prev
            add_node.next = q.next
            q.prev.next = add_node
            q.next.prev = add_node
            return head
        else:
            q = q.next
            order += 1
    q.prev.next = add_node
    add_node.prev = q.prev
    return head


def get_linked_list(head):
    q = head.next
    while q:
        print(q.data, end=" ")
        q = q.next
    print()


def get_result(head, index):
    q = head.next
    order = 0
    while q:
        if order == index:
            return q.data
        else:
            q = q.next
            order += 1
    return -1


T = int(input())
data = []
for _ in range(T):
    n, m, l = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    changes = []
    for __ in range(m):
        tmp = input().split()
        add = list(map(int, tmp[1:]))
        changes.append([tmp[0], add])
    data.append((n, m, l, numbers, changes))


def sol(case):
    n, m, l, numbers, changes = case
    head = Node(-1)
    for i in numbers:
        head = append(head, i)
    for change in changes:
        # print("before")
        # get_linked_list(head)
        method, index_and_data = change
        if method == "I":
            head = insertion(head, index_and_data[0], index_and_data[1])
        elif method == "D":
            head = delete(head, index_and_data[0])
        else:
            head = interchange(head, index_and_data[0], index_and_data[1])
        # print("after")
        # get_linked_list(head)
    return get_result(head, l)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
