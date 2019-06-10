# 백트래킹

## 백트래킹 기법의 정의

백트래킹(Backtracking):해를 찾는 도중에 '막히면', (즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법

- 최적화(Optimization) 문제
- 결정(Decision) 문제를 해결할 수 있음
  - 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'로 답하는 문제
    - 미로 찾기
    - n-Queen 문제
    - Map coloring
    - 부분 집합의 합(Subset Sum) 문제 등

## 백트래킹 - 미로 찾기

백트래킹 기법 활용 - 미로 찾기

1. 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
2. 이동할 수 있는 방향은 4방향으로 제한

## 백트래킹 알고리즘의 특징

- 백트래킹과 깊이 우선 탐색의 차이

|                           백트래킹                           |                        깊이 우선 탐색                        |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 | N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 처리가 불가능함 |
|                      가지치기(Prunning)                      |                       모든 경로를 추적                       |
|                  불필요한 경로의 조기 차단                   |                       모든 후보를 검사                       |
| N! 가지의 경우의 수를 가진 문제에 대해 백트래킹을 가하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능 |                                                              |
|                  모든 후보를 검사하지 않음                   |                                                              |

- 백트래킹 기법
  - 어떤 노드의 유망성을 점검한 후에 유망(Promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(Backtracking) 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 함
  - 반대로 해답의 가능성이 있으면 유망하다고 함
  - 가지치기(Pruning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않음
- 백트래킹을 이용한 알고리즘의 절차
  1. 상태 공간 Tree의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속

## 백트래킹 알고리즘

- 일반 백트래킹 알고리즘
  - n * n의 정사각형 안에 n개의 queen을 배치하는 문제로, 모든 queen은 자신의 일직선상 및 대각선상에 아무 것도 놓이지 않아야 함

~~~python
def checknode(v): # node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
~~~

- 깊이 우선 검색 VS 백트래킹
  - 순수한 깊이 우선 탐색
    - 시간이 많이 걸림
  - 백트래킹
    - 시간이 적게 걸림

## Power Set

- Power Set
  - 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
  - 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 $$2^n$$이 나옴
- 백트래킹 기법으로 Power Set 구하기
  - 일반적인 백트래킹 접근 방법 이용
  - n개의 원소가 들어있는 집합의 $$2^n$$개의 부분집합을 만들 때, True 또는 False값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법 이용
  - 리스트의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

- Power Set을 구하는 백트래킹 알고리즘

~~~python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다.
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    print("(", end="")
    for i in range(k+1):
        if a[i]:
            print(i, end=" ")
    print(")")

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
~~~

- 순열을 구하는 백트래킹 알고리즘

~~~python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k + 1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX
    
    for i in range(1, k):
        in_perm[a[i]] = True
    
    ncandidates = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
        return ncandidates
~~~



