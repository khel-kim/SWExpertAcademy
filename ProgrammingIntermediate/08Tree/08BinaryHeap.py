def insertion(heap, data):
    heap.append(data)
    index = len(heap) - 1
    # print(heap, index)
    while index // 2 != 0:
        # print("before", heap)
        compare_index = index // 2
        if heap[compare_index] >= heap[index]:
            heap[compare_index], heap[index] = heap[index], heap[compare_index]
            index = compare_index
        else:
            break
        # print("after", heap)
    return heap


def sol(case):
    n = case[0]
    numbers = case[1]
    heap = [0, numbers.pop(0)]
    while numbers:
        # print("#"*100)
        # print(heap)
        heap = insertion(heap, numbers.pop(0))
        # print("#" * 100)
        # print(heap)
    # print(heap)

    last_index = len(heap) - 1
    sum = 0
    while last_index // 2 != 0:
        last_index = last_index // 2
        # print(heap[last_index])
        sum += heap[last_index]
    return sum


T = int(input())
data = []
for _ in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    data.append((n, numbers))

for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
