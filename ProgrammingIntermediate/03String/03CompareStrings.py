T = int(input())
data = []
for _ in range(T):
    str1 = input()
    str2 = input()
    data.append([str1, str2])


def search(str1, window):
    start = len(str1)
    index = list(range(len(str1) - 1, -1, -1))
    # print(str1, window)
    for i in index:
        if str1[i] == window[i]:
            result = 1
        else:
            result = 0
            current = window[i]
            # print(current, 'current')
            for j in index:
                if str1[j] == current:
                    start = i - j
                    break
            break
    return start, result


def sol(str1, str2):
    start = 0
    while True:
        end = len(str1) + start
        if end > len(str2):
            return 0
        tmp, result = search(str1, str2[start:end])
        # print(tmp, result)
        start += tmp
        if result == 1:
            return 1
        # print(result)


for i, strings in enumerate(data):
    str1 = strings[0]
    str2 = strings[1]
    print("#%s" %(i + 1), sol(str1, str2))

# print(sol("rithm", "a pattern matching algorithm"))
