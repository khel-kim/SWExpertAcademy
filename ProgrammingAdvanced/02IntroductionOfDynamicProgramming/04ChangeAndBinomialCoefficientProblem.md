# 동전 거스름돈 문제와 이항 계수 문제

### 동전 거스름돈 문제에 동적 계획법 적용

- 사용할 수 이는 동전의 종류 - 1원, 4원, 6원
- 그리디 방법이 항상 최적해를 구할 수 없기 때문에 다른 방법으로 문제 해결
  - 완전 검색 방법
  - 동적 계획법

### 거스름돈 8원에 대한 재귀적인 알고리즘

3가지 동전 각각을 선택해서 재귀적으로 해결

- 1원 동전 한 개 + 7원에 대한 최적해
- 4원 동전 한 개 + 4원에 대한 최적해
- 6원 동전 한 개 + 2원에 대한 최적해

위의 3가지 해 중 최적해를 선택

7원에 대한 최적해는 다시 1원, 4원, 6원 동전을 선택하고 나머지 액수에 대한 최적해

상태 공간 트리의 단말 노드를 모두 방문하게 되면 중복된 작업을 하게 됨

### 중복을 피하기 위해 재귀 알고리즘에 메모이제이션 적용

~~~python
# change: 거스름돈 금액, coin = [6, 4, 1]: 동전 종류
# memo: 이미 구한 부분 문제의 해를 저장, memo[0] = 0 나머지는 -1로 초기화
def CoinChange(change):
    if memo[change] != -1:
        return memo[change]
    else:
        min = INF
        for i in range(len(coin)):
            if change - coin[i] >= 0:
                ret = CoinChange(change - coin[i])
                if min > ret: min = ret
        memo[change] = min + 1
        return memo[change]
~~~

### 동적 계획법 접근: 상향식

1. 1원에 대한 최적해
2. (선택) 2원에 대한 최적해
3. (선택) 3원에 대한 최적해
4. (선택) 4원에 대한 최적해
5. ...

부분 문제들 사이의 의존성

문재를 재귀적으로 구하는 과정에서 찾음

$$f(n) = min\{f(n-6), f(n-2), f(n-1)\} + 1$$

### 동전 거스름돈의 최적해를 상향식으로 구하는 알고리즘

~~~python
# change: 거스름돈 금액, coin = [6, 4, 1]: 동전 종류
# memo: 이미 구한 부분 문제의 해를 저장

def CoinChange_DP(change):
    for N in range(1, change + 1):
        min = INF
        for i in range(len(coin)):
            if N >= coin[i]:
                ret = memo[N - coin[i]]
                if min > ret: min = ret
        memo[N] = min + 1
    return memo[change]
~~~

### 재귀 호출을 이용해서 이항 계수를 구하는 알고리즘

~~~python
def bino(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return bino(n-1, k-1) + bino(n-1, k)
~~~

다수의 중복 호출 존재

### 메모이제이션을 이용한 이항 계수의 계산

~~~python
# B: 이미 구한 부분 문제의 해를 저장, -1로 초기화

def bino1(n, k):
    if k == 0 or k == n: return 1
    if B[n][k] != -1:
        return B[n][k]
    else:
        B[n][k] = bino1(n-1, k-1) + bino1(n-1, k)
        return B[n, k]
~~~

### 동적 계획법을 적용한 이항계수 계산: O(nk)

~~~python
# B: 이미 구한 부분 문제의 해를 저장

def bino2(n, k):
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]
~~~

