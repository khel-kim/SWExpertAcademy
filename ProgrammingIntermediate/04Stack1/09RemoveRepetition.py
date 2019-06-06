T = int(input())
data = []
for _ in range(T):
    data.append(input())

# print(data)
# case = data[0]
# sol
def sol(case):
    case = list(case)
    stack = []
    while True:
        for i in case:
            # print(stack)
            if not stack:
                stack.append(i)
                continue
            top = stack[-1]
            if top == i:
                stack.pop(-1)
                continue
            else:
                stack.append(i)
        # print(case, stack)
        if case == stack:
            break
        else:
            case = stack
            stack = []
    return len(case)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
