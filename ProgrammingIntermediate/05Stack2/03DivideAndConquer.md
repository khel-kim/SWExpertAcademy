# 분할 정복

## 분할 정복 알고리즘

설계 전략

1. 분할(Divide)
   1. 해결할 문제를 여러 개의 작은 부분으로 나눔
2. 정복(Conquer)
   1. 나눈 작은 문제를 각각 해결
3. 통합(Combine)
   1. (필요하다면) 해결된 해답을 모음

분할 정복 기반의 알고리즘:

~~~python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
    else:
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base
~~~

## 퀵 정렬

|        | 합병 정렬                                               | 퀵정렬                                                 |
| ------ | ------------------------------------------------------- | ------------------------------------------------------ |
| 공통점 | 주어진 리스트를 두 개로 분할하고, 각각을 정렬           | 주어진 리스트를 두 개로 분할하고, 각각을 정렬          |
| 차이점 | 각 부분 정렬이 끝난 후, '합병'이란 후처리 작업이 필요함 | 각 부분 정렬이 끝난 후, 후처리 작업이 필요로 하지 않음 |

~~~python
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
        
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1
        while(a[R] >= a[pivot] and L < R): R -= 1
        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
~~~

| 알고리즘    | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고                                                 |
| ----------- | ------------- | ------------- | ------------- | ---------------------------------------------------- |
| 버블 정렬   | $$O(n^2)$$    | $$O(n^2)$$    | 비교와 교환   | 코딩이 가장 손쉬움                                   |
| 카운팅 정렬 | $$O(n + k)$$  | $$O(n + k)$$  | 비교환 방식   | n이 비교적 작을 때만 가능                            |
| 선택 정렬   | $$O(n^2)$$    | $$O(n^2)$$    | 비교와 교환   | 교환의 회수가 버블, 삽입정렬보다 작음                |
| 퀵 정렬     | $$O(n logn)$$ | $$O(n^2)$$    | 분할 정복     | 최악의 경우 $$O(n^2)$$이지만, 평균적으로는 가장 빠름 |
| 삽입 정렬   | $$O(n^2)$$    | $$O(n^2)$$    | 비교와 교환   | n의 개수가 작을 때 효과적                            |
| 병합 정렬   | $$O(n logn)$$ | $$O(n logn)$$ | 분할 정복     | 연결 List의 경우 가장 효율적인 방식                  |

