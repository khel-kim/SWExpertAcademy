T = int(input())
data = []
for _ in range(T):
    data.append(int(input()))


def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sol(num):
    quotient = num // 2
    remainder = num % 2
    count = 0
    while quotient:
        n_candi = factorial(quotient+remainder) / (factorial(quotient) * factorial(remainder))
        #print(n_candi, num, quotient, remainder)
        count += n_candi * (2 ** quotient)
        quotient -= 1
        remainder += 2
    count += 1
    return int(count)


for i, num in enumerate(data):
    num = num / 10
    print("#%s" % (i + 1), sol(num))
