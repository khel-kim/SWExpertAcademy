T = int(input())
data = []
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    data.append(arr)

arr = data[0]
# sol
def selection_algorithm(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index]= arr[min_index], arr[i]
    return arr

def sol(arr):
    sort_arr = selection_algorithm(arr)
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(sort_arr[-(i // 2 + 1)])
        else:
            result.append(sort_arr[i // 2])
    return result

for i, arr in enumerate(data):
    print("#%s" % (i + 1), end=' ')
    result = sol(arr)
    for j in result:
        print(j, end=" ")
    print()