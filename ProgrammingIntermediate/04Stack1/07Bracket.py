T = int(input())
data = []
for _ in range(T):
    data.append(input())

# print(data)
# case = data[2]

def sol(case):
    left_bracket = ["{", "("]
    right_bracket = ["}", ")"]
    pair = [("{", "}"), ("(", ")")]
    stack = []
    for i in case:
        # print(stack)
        if i in left_bracket:
            stack.append(i)
        elif i in right_bracket:
            if len(stack) == 0: return 0
            tmp = stack.pop(-1)
            if (tmp, i) not in pair: return 0
    if stack:
        return 0
    return 1


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
