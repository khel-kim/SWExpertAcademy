T = int(input())
data = []
for _ in range(T):
    n = int(input())
    number = list(map(int, list(input())))
    data.append(number)

####################
def sol(arr):
    set_arr = list(set(arr))
    pair_list = []
    for i in set_arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        pair_list.append((i, count))
    return sorted(pair_list, key=lambda x: (x[1], x[0]), reverse=True)

for i, arr in enumerate(data):
    final_list = sol(arr)
    #print(arr, sol(arr))
    print("#%s" %(i + 1), final_list[0][0], final_list[0][1])