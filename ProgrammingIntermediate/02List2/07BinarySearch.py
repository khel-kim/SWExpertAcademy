T = int(input())
data = []
for _ in range(T):
    tmp = list(map(int, input().split()))
    data.append(tmp)

# sol1
def binary_search1(p, a):
    start = 1
    end = p
    count = 0
    while True:
        count += 1
        middle = int((start + end) / 2)
        if middle == a:
            return count
        elif middle < a:
            start = middle
        else:
            end = middle

def sol1(arr):
    p, a, b = arr
    a_count = binary_search1(p, a)
    b_count = binary_search1(p, b)
    if a_count == b_count:
        return 0
    elif a_count < b_count:
        return "A"
    else:
        return "B"

for i, arr in enumerate(data):
    print("#%s" % (i + 1), sol1(arr))

# sol2
def binary_search2(start, end, a, count=0):
    middle = int((start + end) / 2)
    count += 1
    if a == middle:
        return count
    elif a > middle:
        return binary_search2(middle, end, a, count)
    else:
        return binary_search2(start, middle, a, count)



def sol2(arr):
    p, a, b = arr
    a_count = binary_search2(1, p, a)
    b_count = binary_search2(1, p, b)
    if a_count == b_count:
        return 0
    elif a_count < b_count:
        return "A"
    else:
        return "B"

for i, arr in enumerate(data):
    print("#%s" % (i + 1), sol2(arr))