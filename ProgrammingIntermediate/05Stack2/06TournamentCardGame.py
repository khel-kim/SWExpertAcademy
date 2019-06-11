T = int(input())
data = []
for _ in range(T):
    n = int(input())
    case = list(map(int, input().split()))
    data.append(case)



def sol(case):
    case_with_index = []
    for i, RSP in enumerate(case):
        case_with_index.append([i + 1, RSP])
    return divide(case_with_index)


def divide(case_with_index):
    if len(case_with_index) == 0:
        return
    elif len(case_with_index) == 1:
        return case_with_index[0]
    elif len(case_with_index) == 2:
        a = case_with_index[0][1]
        b = case_with_index[1][1]
        if abs(a - b) == 1:
            return sorted(case_with_index, key=lambda x: x[1], reverse=True)[0]
        elif abs(a - b) == 2:
            return sorted(case_with_index, key=lambda x: x[1])[0]
        else:
            return case_with_index[0]
    else:
        n = len(case_with_index)
        left = case_with_index[:n // 2]
        right = case_with_index[n // 2:]
        print(left, right, 11111111111111)
        left_side = divide(left)
        right_side = divide(right)
        print(left_side, right_side)
        print(calculator(left_side, right_side),132165465498798)
        return calculator(left_side, right_side)


def calculator(arr1, arr2):
    if abs(arr1[1] - arr2[1]) == 1:
        return sorted([arr1, arr2], key=lambda x: x[1], reverse=True)[0]
    elif abs(arr1[1] - arr2[1]) == 2:
        return sorted([arr1, arr2], key=lambda x: x[1])[0]
    else:
        return arr1


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case)[0])
