T = int(input())
data = []
for _ in range(T):
    N = int(input())
    tmp = [int(i) for i in input().split()]
    data.append(tmp)

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]: continue
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

for i, nums in enumerate(data):
    arr = bubble_sort(nums)
    print('#%s' %i, arr[-1] - arr[0])