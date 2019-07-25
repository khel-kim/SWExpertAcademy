# 순회 외판원 문제

## 소개

### 순회 외판원 문제(Traveling Salesman Problem)

1. 외판원이 자신의 집이 위치하고 있는 도시에서 출발
2. 다른 도시들을 각각 한번씩만 방문
3. 다시 자기 도시로 돌아오는 가장 짧은 일주여행경로(Tour) 결정
4. TSP로 줄여서 부름

1. 대상: 음이 아닌 가중치가 있는, 방향성 그래프
2. 그래프 상에서 일주여행경로: 한 정점을 출발하여 다른 모든 정점을 한번씩만 거쳐서 다시 그 정점으로 돌아오는 경로
3. 최적일주여행경로(Optimal tour): 여러 개의 일주여행경로 중에서 길이가 최소가 되는 경로

### 무작정 알고리즘

가능한 모든 일주여행경로를 고려한 후, 그 중에서 가장 짧은 일주여행경로 선택

## 동적 계획법 기반 알고리즘

### 순회 외판원 문제를 해결하는 동적 계획법 알고리즘

- V는 모든 정점의 집합이고, A는 V의 부분집합
- $$D[v_i][A]$$는 $$A$$에 속한 각 정점을 정확히 한번씩만 거쳐서 $$v_i$$에서 $$v_1$$으로 가는 최단경로
- $$D[v_1][V-\{v_1\}] = min_{2 \leq j \leq n}(W[1][j] + D[v_j][V-\{v_1, v_j\}])$$
- $$D[v_i][A] = min_{v_i \in A}(W[i][j] + D[v_j][A - \{v_j\}]) if A \neq \empty$$
- $$D[v_i][\empty] = W[i][1]$$

```python
# W: 인접 행렬, minlength: 최적일주여행경로의 가중치 합, n: 정점의 개수
# D: 부분 문제의 해를 저장하기 위한 저장소
def travel(n, W):
    numer D[1 .. n][subset of V - {v1}]
    
    for i in 2 -> n:
        D[i][emptyset] <- W[i][1]
        
    for k in 1 -> n - 2:
        for all subsets A in V - {v1} containing k vertices:
            for i such that i != and vi not in A:
                D[i][A] = minimun_(vj in A)(W[i][j] + D[vj][A - {vj}])
    
    D[1][V - {v1}] = minimum(2 <= j <= n)(W[1][j] + D[vj][A - {v1}])
    minlenght = D[1][V - {v1}]
```

