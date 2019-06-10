T = int(input())
data = []
for _ in range(T):
    data.append(input())


def calculator(a, b, symbol):
    if symbol == "+":
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "*":
        return a * b
    else:
        return int(a / b)


def sol(case):
    symbols = ["+", "-", "*", "/"]
    stack = []
    case = case.split()
    for i in case:
        if i not in symbols + ["."]:
            stack.append(int(i))
        else:
            if i == ".":
                if len(stack) != 1: return "error"
                return stack[0]
            else:
                try:
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    result = calculator(a, b, i)
                    stack.append(result)
                except IndexError:
                    return "error"


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
