def back_tracking():
    global location, result, best
    if location >= n-1:
        best = len(visit)
        result.append(len(visit))
        # print(len(visit),visit, 'asdfasdf')
        # print(result)
    else:
        current = station[location]
        for step in range(current, 0, -1):
            location += step
            if location >= n - 1:
                back_tracking()
                location -= step
            else:
                visit.append(station[location])
                if len(visit) >= best:
                    visit.pop()
                    location -= step
                    continue
                back_tracking()
                visit.pop()
                location -= step


def sol(case):
    global location, result, visit, station, n, best
    n, station = case
    location = 0
    visit = [station[location]]
    result = []
    best = n
    back_tracking()
    # print(result)
    return min(result) - 1


T = int(input())
data = []
for _ in range(T):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    station = tmp[1:]
    data.append((n, station))

for i, case in enumerate(data):
    print("#%s" % (i + 1), sol(case))
