T = int(input())
data = []
for _ in range(T):
    str1 = input()
    str2 = input()
    data.append([str1, str2])


def sol(str1, str2):
    str_list1 = list(str1)
    str_list2 = list(str2)

    str_set = list(set(str_list1))
    counts = []
    for i in str_set:
        count = 0
        for j in str_list2:
            if i == j:
                count += 1
        counts.append(count)
    return max(counts)


for i, strings in enumerate(data):
    print("#%s" % (i + 1), sol(strings[0], strings[1]))