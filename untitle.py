def CoinChange(change):
    print(memo)
    if memo[change] != -1:
        return memo[change]
    else:
        min = 1000
        for i in range(len(coin)):
            if change - coin[i] >= 0:
                ret = CoinChange(change - coin[i])
                if min > ret: min = ret
        memo[change] = min + 1
        return memo[change]


memo = [-1] * 10
coin = [6, 4, 1]
print(CoinChange(8))
memo = [-1] * 20
count = 0
memo[0] = 0
# memo[1] = 1


def coin_change(change):
    print(memo)
    if memo[change] != -1:
        return memo[change]
    else:
        min = change + 1
        for i in range(len(coin)):
            if change - coin[i] >= 0:
                tmp = coin_change(change - coin[i])
                if min > tmp: min = tmp
        memo[change] = min + 1
        return memo[change]


print(coin_change(10))

def CoinChange_DP(change):
    for N in range(1, change + 1):
        print(memo)
        min = 100000
        for i in range(len(coin)):
            if N >= coin[i]:
                ret = memo[N - coin[i]]
                if min > ret: min = ret
        memo[N] = min + 1
    return memo[change]

print(CoinChange_DP(8), 'asdfsadfas')