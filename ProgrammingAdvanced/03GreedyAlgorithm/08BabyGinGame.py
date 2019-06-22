T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, input().split())))


def is_run(count):
    for i, value in enumerate(count):
        if value >= 3:
            count[i] -= 3
            return True
    return False


def is_triplet(count):
    if len(count) < 3:
        return False
    else:
        for i in range(len(count) - 2):
            if count[i] > 0 and count[i + 1] > 0 and count[i + 2]:
                count[i] -= 1
                count[i + 1] -= 1
                count[i + 2] -= 1
                return True
        return False


def check(count):
    check1 = is_run(count)
    check2 = is_triplet(count)
    # print(check1, check2)
    if check1 or check2:
        return True
    else:
        return False


def sol(case):
    card = case
    player1 = []
    player2 = []
    count1 = [0 for _ in range(10)]
    count2 = [0 for _ in range(10)]
    num = 0
    result1 = False
    result2 = False
    while card:
        current = card.pop(0)
        if num % 2 == 0:
            player1.append(current)
            count1[current] += 1
            result1 = check(count1)
            if result1:
                break
        else:
            player2.append(current)
            count2[current] += 1
            result2 = check(count2)
            if result2:
                break
        num += 1
    # print(player1, player2)
    # print(result1, result2)
    if result1:
        return 1
    elif result2:
        return 2
    else:
        return 0


for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
