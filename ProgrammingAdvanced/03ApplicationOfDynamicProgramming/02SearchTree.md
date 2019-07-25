# 상태 공간 트리의 탐색

### 상태 공간 트리의 탐색

- 문제 해결 과정의 중간 상태를 각각 한 노드로 나타낸 트리

### 상태 공간 트리의 3가지 탐색 방법

- 깊이 우선 탐색 - Depth-First Search (Backtracking)
- 너비 우선 탐색 - Breadth-First Search
- 최고 우선 탐색 - Best-First Search(A* algorithm)

### 세 가지 탐색 방법을 배낭 문제에 대한 상태 공간 트리에 적용

## 분기 한정

### 분기 한정(Branch and Bound)

- 상태 공간 트리를 탐색하는 과정에서 최적해를 찾을 가능성이 없다고 판단되면 가지치기 수행
- 지금까지 찾은 가장 좋은 해보다 더 좋은 해를 찾을 수 있는가에 대해서 판단
  - 판단을 위해 어떤 전략을 사용하는지에 따라서 분기한정의 효율성 좌우
- 상태 공간 트리의 노드를 방문할 때마다, 그 노드의 유망성을 판단하기 위해 한계치(bound) 계산
  - 한계치: 해당 노드에서 계속 탐색을 수행하면 얻을 수 있는 후보 해답의 최대치
- 한계치가 지금까지 찾은 최적의 값보다 좋지 않으면 유망하지 않다고 판단

## 분기 한정 깊이 우선 탐색

### 분기 한정 가지치기로 깊이 우선 탐색(= 백트래킹)

- 상태 공간 트리를 구축하여 백트래킹 기법으로 문제 풀이
- 루트 노드에서 왼쪽으로 가면 첫 번째 물건을 배낭에 넣는 경우이고, 오른쪽으로 가면 첫 번째 물건을 배낭에 넣지 않는 경우
- 트리의 높이(수준) 1에서 왼쪽으로 가면 두 번째 물건을 배낭에 넣는 경우이고, 오른쪽으로 가면 그렇지 않은 경우
- 계속하여 상태 공간 트리 구축하면, 루트 노드로부터 단말 노드까지의 모든 경로는 해답 후보가 됨
- 최적의 해를 찾는 문제(Optimization problem)의 경우 검색이 완전히 끝나기 전에는 해답을 알 수가 없음
- 검색을 하는 과정 동안 항상 그때까지 찾은 최적해를 기억해야(메모리에 저장)함

### 상태 공간 트리를 깊이 우선 탐색하면서 분기 한정을 적용한 알고리즘

~~~python
# best: 지금까지 찾은 최대 가치
# value(v): 노드 v에서의 가치

def checknode(node v):
    if best < value(v):
        best = value(v)
    if promising(v):
        for u in v.child:
            checknode(u)
~~~

### 배낭 문제에서 분기 한정 적용을 위한 한계치 계산 방법

- $$w_i$$와 $$p_i$$를 각각 $$i$$번째 물건의 무게와 가치라고 하면, 무게 당 가치($$p_i/w_i$$)의 값이 큰 것부터 내림차순으로 물건 정렬
- 방문하는 노드에서 다음 값들에 대해서 계산
  - profit: 해당 노드에 오기까지 넣었던 물건들의 가치의 합
  - weight: 해당 노드에 오기까지 넣었던 물건들의 무게의 합
  - bound(한계치): 노드가 수준 $$i$$에 있고, 수준 $$k$$에 있는 노드에서 총무게가 $$W$$를 넘는다고 할 경우, 다음과 같이 bound를 구할 수 있음
    - $$totweight = weight + \sum^{k-1}_{j=i+1}W_j$$
    - $$bound = [profit + \sum^{k-1}_{j=i+1}p_j] + (W - totweight) \times \frac{p_k}{w_k}$$
  - maxprofit: 지금까지 찾은 최선의 해답이 주는 가치

### 방문하는 노드의 바운드를 계산해서 가지치기 하는 과정

- 초기값(루트 노드)
  - maxprofit = 0, profit = 0, weight = 0
- 깊이 우선순위로 각 노드를 방문하여 다음을 수행
  - 해당 노드의 profit과 weight를 계산
  - 해당 노드의 bound를 계산
  - weight \< W and bound \> maxprofit이면, 탐색을 계속함; (무게가 초과하지 않았고, 향후 가치가 최대 가치보다 클 수 있다면) 그렇지 않으면, 되돌아 다시 추적
- 상기 과정을 모든 노드를 방문(실제로는 전지(가지치기)가 이뤄지므로, 모든 노드를 방문하지는 않음)할 때까지 수행
- 최선이라고 여겼던 노드를 선택해서 탐색을 수행한다고 해서 최적해를 찾을 수 있다는 보장은 없음

### 깊이 우선 탐색을 수행할 경우 점검하는 노드의 수

- 알고리즘이 점검하는 노드의 수 - $$\Theta(2^n)$$
- 예제) 점검한 노드는 13개. 이 알고리즘이 동적 계획법 기반으로 설계한 알고리즘 보다 좋은가?
  - 확실한 대답 불가능

## 분기 한정 너비 우선 탐색

- 재귀(Recursive) 알고리즘 작성은 복잡함
- 대기 열(Queue) 사용

~~~python
# Q: 큐
# T: 상태공간트리
# v: root of T

def breadth_first_search(T, v):
    initialize(Q)
    visit(v)
    enqueue(v)
    while Q:
        v = dequeue()
        for u in v.child:
            visit(u)
            enqueue(u)
~~~

### 너비 우선 탐색에 분기 한정을 적용한 알고리즘

~~~python
# Q: 큐, T: 상태공간트리. v: root of T
# best: 지금까지 찾은 최대 가치
# value(v): 노드 v에서의 가치

def breadth_first_branch_and_bound(T, v):
    initialize(Q)
    visit(v)
    enqueue(v)
    best = value(v)
    while Q:
        v = dequeue()
        for u in v.child:
            if best < value(u):
                best = value(u)
            if best < bound(u):
                visit(u)
                enqueue(u)
~~~

### 백트래킹 알고리즘(DFS 기반 해결책)보다 좋지 않음

## 최고 우선 탐색

### 최적의 해답에 더 빨리 도달하기 위한 전략

- 주어진 노드의 모든 자식노드 탐색
- 유망하면서 확장되지 않은(Unexpanded) 노드 확인
- 가장 좋은(최고의) 한계치(bound)를 가진 노드 확장
  - 최고 우선 탐색(Best-First Search)
    - 너비 우선 탐색에 비해서 탐색 성능 좋아짐

최고 한계치를 가진 노드를 우선 선택하기 위해서 우선순위 대기열(Priority Queue) 사용

- 우선순위 대기열은 힙(Heap)을 사용하여 효과적으로 구현
- 최적해를 빨리 찾을수록 가지치기를 효율적으로 수행함으로써 탐색 시간을 줄일 수 있음

~~~python
# PQ: 우선 순위 큐, T: 상태공간트리, v: root of T
# best: 지금까지 찾은 최대 가치
# value(v): 노드 v에서의 가치

def best_first_branch_and_bound(T, v):
    initialize(PQ)
    best = value(v)
    visit(v)
    insert(v)
    while PQ:
        v = remove()
        if best < bound(v):
            for u in v.child:
                if best < value(u):
                    best = value(u)
                if best < bound(u):
                    visit(u)
                    insert(u)
~~~

분기 한정 가지치기로 최고우선검색을 하여 상태 공간 트리를 그려보면, 검색하는 노드의 개수는 11로서, BFS보다 우수함을 알 수 있음

### 최고 우선 탐색의 단점

- 최적해를 빠른 시간에 찾는다고 보장 못함
  - 일반적으로 최적해는 상태 공간 트리의 깊은 곳에 존재할 가능성 높음
- 노드 설정(Node setup) 비용이 큼
  - 최적해를 찾을 가능성이 높은 노드를 평가해서 다음 노드로 가기 위한 비용을 최소화 함
- 메모리 사용량이 매우 큼
  - 후보 노드들의 리스트를 저장하기 위해서 많은 메모리가 요구됨