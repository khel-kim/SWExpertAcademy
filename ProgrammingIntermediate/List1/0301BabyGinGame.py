def permutation(arr, m):
    visit = []
    tmp_arr = []
    for i, j in enumerate(arr):
        tmp_arr.append((i, j))
    def generator(arr, m):
        if len(visit) == m:
            yield visit
        else:
            for j in range(len(arr)):
                if arr[j] in visit:
                    continue
                visit.append(arr[j])
                yield from generator(arr, m)
                visit.pop()
    yield from generator(tmp_arr, m)


given_num = [1, 7, 3, 2, 7, 7]

def check(num):
    if num[1] - num[0] == 1 and num[2] - num[1] == 1:
        return True
    elif len(set(num)) == 1:
        return True
    else:
        return False

def get_babygin(num):
    first = num[:3]
    second = num[3:]
    return check(first) and check(second)


for nums in permutation(given_num, 6):
    numbers = []
    for i, j in nums:
        numbers.append(j)
    checker = get_babygin(numbers)
    if checker:
        break
print(checker)