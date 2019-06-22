# 퀵 정렬

## 소개

### 퀵 정렬

- 주어진 리스트를 두 개로 분할하고, 각각을 정렬
- 병합 정렬과 동일해 보이나 다른 점을 가짐
- 병합 정렬
  - 두 부분으로 나눔
  - 각 부분 정렬이 끝난 후, 병합하는 후처리 작업 필요
- 퀵 정렬
  - 분할 시, 기준 아이템(Pivot item) 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치
  - 각 부분 정렬이 끝난 후, 병합하는 후처리 작업이 불필요

## 알고리즘

### 퀵 정렬 알고리즘의 동작 과정

~~~python
# A: 리스트, ㅣ: 시작 인덱스, r: 끝 인덱스
def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)
~~~

## Hoare 파티션

### 호어 파티션 알고리즘의 아이디어

- P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치 시킴
- 피봇을 두 집합의 가운데에 위치시킴
  - 피봇이 위치한 곳은 정렬된 상태일 때, 자기가 있어야 할 위치에 놓임
  - 피봇 값은 다음 정렬 과정에서 제외

### Hoare-Partition 알고리즘

~~~python
def partition(A, l, r):
    p = A[l]
    i = l + 1
    j = r
    while i <= j:
        while(i <= j and A[i] <= p): i += 1
        while(i <= j and A[j] >= p): j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j
~~~

### 피봇 선택

- 왼쪽 끝/ 오른쪽 끝/ 임의의 세 개 값 중에 중간 값

## Lomuto 파티션

### 로무토 파티션

- i와 j 두 개의 변수를 사용하며, i와 j가 모두 증가하면서 작업 수행

~~~python
def partition(A, l, r):
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
~~~

i: 피봇 보다 작은 마지막 값의 인덱스

j: 피봇 보다 큰 마지막 값의 인덱스