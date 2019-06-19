T = int(input())
data = []
for _ in range(T):
    n, numbers = input().split()
    numbers = list(numbers)
    data.append(numbers)


def transformer(component):
    numbers = [str(i) for i in range(10)]
    numbers.extend(list("ABCDEF"))
    binary_number = []
    for i in range(16):
        binary_number.append(bin(i)[2:].rjust(4, "0"))
    return binary_number[numbers.index(component)]


def sol(case):
    result = []
    for i in case:
        result.append(transformer(i))
    return "".join(result)


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
