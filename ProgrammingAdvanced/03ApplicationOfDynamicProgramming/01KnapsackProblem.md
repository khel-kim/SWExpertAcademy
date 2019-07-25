# 배낭문제

## 소개

### 0-1 배낭 문제에 동적 계획법 적용하기

- 배낭 문제(Knapsack) 문제

## 완전 검색

### 배낭 문제에 대한 완전 검색 방법

- 완전 검색으로 물건들의 집합 S에 대한 모든 부분집합 구함
- 부분집합에 포함된 물던들의 총 무게가 배낭 무게 W를 초과하는 집합들은 버리고, 나머지 집합에서 총 값이 가장 큰 집합 선택
- 부분집합을 생성하는 상태공간 트리를 탐색하는 방법으로 모든 후보해 탐색

~~~python
# W: 남은 배낭의 무게, k: 배낭에 넣을 물건(1, ..., n), 방문하는 노드의 높이
# curValue: 현재까지 담은 물건의 총 가치, maxValue: 최대 가치
# n: 물건의 개수

def knapsack(W, k, curValue):
    global maxValue
    if W >= 0:
        if k > n:
            if maxValue < curValue:
                maxValue = curValue
        else:
            knapsack(W - weight[k], k+1, curValue + value[k])
            knapsack(W, k+1, curValue)
~~~

## 부분 문제 정의

### 배낭 문제 완전 검색 방법 - 부분 문제 정의

### 배낭 문제에 대한 재귀적 정의의 점화식 표현

- w = 배낭의 용량(kg)

- n개의 물건들의 집합 = {1, 2, . . ., n}

- $$(v_i, w_i)$$ = 물건 가치(만원), 무게(kg). ($$1 \leq i \leq n$$)

- K[i]\[w\] = 물건 1~i까지만 고려하고, (임시) 배낭의 용량이 w일 때의 최대 가치
  - 단, i = 1, 2, . . ., n이고, w = 1, 2, 3, . . ., W

- K[i]\[w\]의 재귀적 정리

- K[i]\[w\] = 0 if i = 0 or w = 0

  ​			= k[i-1]\[w\] if $$w_i$$ > w

  ​			= max( k[i - 1]\[w-$$w_i$$\]] + $$v_i$$, k[i - 1]\[w\]])

### 배낭 문제의 부분 문제 간의 함축적 순서

- 2개의 부분 문제 K[i - 1]\[w - $$w_i$$\]와 K[i - 1]\[w\]가 미리 계산되어 있어야만 K[i]\[w\]가 계산 가능

~~~python
# K[i][W]: 부분 문제의 해(최대가치)를 저장하기 위한 리스트, -1로 초기화
# i: 배낭에 넣을 물건을 나타내는 값(1, ..., n), W: 배낭의 무게
# n: 물건의 개수

def knapsack(i, W):
    if K[i][W] != -1:
        return k[i][W]
    
    if i == 0 or W == 0:
        K[i][W] = 0
    else:
        case1 = 0
        if W >= weight[i]:
            case1 = knapsack(i-1, W-weight[i]) + value[i]
        case2 = knapsack(i-1, W)
        
        K[i][W] = max(case1, case2)
        return K[i][W]
~~~

## 동적 계획법 적용

### 부분 문제의 의존성

i가 0인 공집합부터 시작해서 i값을 증가 시켜가면서 구해 나감

상향식 문제의 해결 - 필요한 부분 문제가 어떤 것들인지 알기 어려워 모든 부분 문제들에 대한 해를 구해 나가야 함

리스트를 행 우선으로 탐색하는 순서로 테이블을 채워 나가면 의존성에 위배되지 않음

### 배낭 문제에 동적 계획법을 적용해서 상향식으로 최적해를 구하는 알고리즘

~~~python
# 배낭의 무게 W
# i: 배낭에 넣을 물건을 나타내는 값(1, ..., n)
# n: 물건의 개수
# 리턴: K[n][W]

def knapsack():
    for i in range(n+1):
        K[i][0] = 0
    for w in range(W+1):
        K[0][w] = 0
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weight[i] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w-weight[i]] + value[i], K[i-1][w])
    return K[n][W]
~~~

