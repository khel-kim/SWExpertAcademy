from collections import deque
T = int(input())
data = []
for _ in range(T):
    n, m = list(map(int, input().split()))
    sequences = []
    for __ in range(m):
        sequence = deque(list(map(int, input().split())))
        sequences.append(sequence)
    data.append((n, m, sequences))


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def add_to_last(head, data):
    add_node = Node(data)
    q = head
    while q.next:
        q = q.next
    q.next = add_node
    add_node.prev = q
    return head


def combine(head1, head2):
    current = head2.next.data
    q = head1
    while q:
        if q.data > current:
            break
        head1_tail = q
        q = q.next
    q2 = head2
    while q2.next:
        q2 = q2.next

    if q is not None:
        q.prev.next = head2.next
        head2.next.prev = q.prev
        q2.next = q
        q.prev = q2
    else:
        head1_tail.next = head2.next
        head2.next.prev = head1_tail
    return head1

def sol(case):
    n = case[0]
    m = case[1]
    sequences = case[2]

    heads = []
    for _ in range(m):
        head = Node(-1)
        heads.append(head)

    for i, sequence in enumerate(sequences):
        while sequence:
            heads[i] = add_to_last(heads[i], sequence.popleft())

    first = heads[0]
    for i in range(m - 1):
        first = combine(first, heads[i + 1])
    return first


for i, case in enumerate(data):
    print("#%s" % (i + 1), end=" ")
    result = sol(case)
    q = result
    while q.next:
        q = q.next
    for _ in range(10):
        print(q.data, end=" ")
        q = q.prev
    print()
