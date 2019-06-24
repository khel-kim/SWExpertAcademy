def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        n = len(arr)
        left = arr[:n // 2]
        right = arr[n // 2:]
        merge_left = merge_sort(left)
        merge_right = merge_sort(right)
        return merge(merge_left, merge_right)


def merge(left, right):
    global count
    if left[-1] > right[-1]: count += 1
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) != 0:
        result.extend(left)
    else:
        result.extend(right)
    return result


def sol(case):
    global count
    n, arr = case
    count = 0
    return merge_sort(arr)[len(arr) // 2], count


T = int(input())
data = []
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    data.append((n, arr))

for i, case in enumerate(data):
    result = sol(case)
    print("#%s" % (i + 1), result[0], result[1])
