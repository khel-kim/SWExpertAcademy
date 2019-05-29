given_nums = [1, 2, 3, 3, 7, 7]

counts = [0 for _ in range(10)]
for num in given_nums:
    counts[num] += 1

checker = [0 for _ in range(10)]
check = True
while counts != checker:
    origin = counts.copy()
    for i, count in enumerate(counts):
        if count >= 3:
            counts[i] -= 3
        if count >= 1:
            if i == 0: continue
            if i == 5: continue
            if counts[i - 1] != 0 and counts[i + 1] != 0:
                counts[i - 1] -= 1
                counts[i] -= 1
                counts[i + 1] -= 1
    if origin == counts:
        check = False
        break
print(check)