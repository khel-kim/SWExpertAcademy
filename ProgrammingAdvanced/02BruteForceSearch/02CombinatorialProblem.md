# 조합적 문제

## 완전 검색과 조합적 문제

### 완전 검색

- 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 검색
- 순열(Permutation), 조합(Combination), 부분집합(Subset)과 같은 조합적 문제들(Combinatorial Problems)과 관련
- 조합적 문제에 대한 고지식한 방법(Brute-force)

## 순열

### 순열

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열 표현

### 다수의 알고리즘 문제들

- 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련됨
  - 순회 외판원 문제(Traveling Salesman Problem)
    - 여러 도시들이 있고 한 도시에서 다른 도시로 이동하는 비용이 모두 주어짐
    - 출발 도시에서 시작해서 다른 모든 도시들을 단 한 번만 방문하고 출발 도시로 돌아오는 최소 비용의 이동경로를 구하는 문제
    - 방문할 도시들을 순서대로 나열하면 하나의 경로가 됨
- N 개의 요소들에 대해서 n!개의 순열들 존재
  - 순회 외판원 문제에서 거쳐가야 할 도시가 n개라면 가능한 모든 경로는 n!만금 존재(12! = 479,001,600)
  - n > 12인 경우, 시간 복잡도 폭발적으로 증가

1. 사전식 순서(Lexicographic-Order)

   - 요소들이 오름차순으로 나열된 형태로 시작하는 하나의 순열

2. 최소 변경을 통한 방법(Minimum-exchange requirement)

   - 각각의 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성

3. 최소한의 변경(Minimum-change requirement)을 통해 순열을 생성하는 방법

   - Johnson-Trotter 알고리즘

4. 두 원소의 교환을 통해 생성

   - 순열이 생성되는 모든 과정을 그리면 트리 구조를 가짐
   - 요소의 수가 네 개로 루트는 자식이 네 개이고 트리의 높이는 1인 내부노드들은 자식이 세 개가 되는 구조의 트리가 됨
   - 네 번의 선택을 하기 때문에 트리의 높이는 4가 됨
   - 트리를 순회하는 것과 같이 재귀 호출을 통해 순열을 생성
   - 트리의 단말에 도착하게 되면 하나의 순열 생성

   ~~~python
   # 재귀 호출을 통한 순열 생성
   def perm(n, k):
       if k == n:
           print(a)
       else:
           for i in range(k, n):
               a[k], a[i] = a[i], a[k]
               perm(n, k + 1)
               a[k], a[i] = a[i], a[k]
   ~~~

### 파이썬의 라이브러리를 활용한 순열

~~~python
import itertools
mylist = [1, 2, 3]
result = itertools.permutations(mylist)

print(list(result))
~~~

### 파이썬의 라이브러리를 활용한 중복 순열

~~~python
import itertools
mylist = [1, 2, 3]
result = itertools.product(mylist, repeat=3)

print(list(result))
~~~

## 부분집합

### 부분집합

- 집합에 포함된 원소들을 선택하는 것
- 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는 것
  - 배낭 짐싸기(Knapsack problem)
    - 배낭과 물건들의 집합이 주어지며, 배낭의 무게가 있고, 아이템들은 각각 무게와 가치가 있음
    - 배낭에 담는 무게의 총합 < 배낭의 무게
    - 물건의 총합이 배낭의 무게를 초과하지 않으면서 가치의 합이 최대가 되는 물건들을 선택하는 문제
- N개의 원소를 포함한 집합
  - 자기 자신과 공집합을 포함한 모든 부분집합(Power set)의 개수는 $$2^n$$개
  - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

### 비트표현을 이용해서 부분집합을 생성하는 간단한 방법

- 바이너리 카운팅을 통한 사전적 순서(Lexicographic Order)
  - 부분집합을 생성하기 위한 가장 자연스럽고 간단한 방법
  - 바이너리 카운팅(binary counting)은 사전적 순서로 생성하기 위한 가장 간단한 방법

- 바이너리 카운팅(Binary Counting)
  - 원소 수에 해당하는 N개의 비트 열을 이용
  - i 번째 비트 값이 1이면 i번째 원소가 포함되었음을 의미

### 바이너리 카운팅을 통한 부분집합 생성 코드

~~~python
arr = [2, 3, 4, 5]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=",")
    print()
~~~

## 조합

### 조합(Combination)

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것

### 재귀 호출을 이용한 조합 생성 알고리즘

~~~python
def comb(n, r):
    if r == 0: print(tr)
    elif n < r: return
    else:
        tr[r - 1] = an [n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)
~~~

### 파이썬의 라이브러리를 활용한 조합

~~~python
import itertools
mylist = [1, 2, 3]
result = itertools.combinations(mylist, r=2)
print(list(result))
~~~

### 파이썬의 라이브러리를 활용한 중복 조합

~~~python
import itertools
mylist = [1, 2, 3]
result = itertools.combinations_with_replacement(mylist, r=2)
print(list(result))
~~~

