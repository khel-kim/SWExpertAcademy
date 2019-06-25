# 동전 거스름돈 문제

### 동전 거스름돈 문제에 대한 예제 코드

백트래킹 기법 적용

~~~python
# coin[]: 동전의 금액을 저장, choice[]: 선택한 동전들 집합
# best: 거스름돈에 대한 최소 동전 개수
def CoinChange(choice, N, money):
    global best
    if best <= N:
        return
    elif money == 0:
        best = N
    else:
        for i in range(len(coin)):
            if money - coin[i] >= 0:
                choice[N] = coin[i]
                CoinChange(choice, N+1, money-coin[i])
~~~

