T = int(input())
data = []
for _ in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    data.append((n, numbers))

case = data[0]
#####


def quick_sort(arr, start, end):
    if start >= end:
        return arr
    else:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    pivot = start
    i = pivot + 1
    j = end
    while i <= j:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while i <= j and arr[j] >= arr[pivot]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


for i, case in enumerate(data):
    n, arr = case
    quick_sort(arr, 0, n-1)
    print("#%s" % (i + 1), arr[n // 2])
