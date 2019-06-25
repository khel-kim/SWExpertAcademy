# 부분 집합

## 소개

### Power set 생성 방법

## 알고리즘

### 부분집합의 상태 공간 트리 -> 깊이 우선 탐색으로 모든 부분집합 생성알고리즘

~~~python
def subset(a, k, n):
    if k == n:
        process_solution(a, n)
    else:
        a[k] = 0
        subset(a, k+1, n)
        a[k] = 1
        subset(a, k+1, n)
~~~

