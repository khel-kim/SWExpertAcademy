# 병합 정렬

## 병합 정렬의 특징

병합 정렬: 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

1. 분할 정복 알고리즘 활용
   1. 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
   2. Top - Down 방식
2. 시간 복잡도
   1. $$O(n log n)$$

## 병합 정렬의 과정

1. 분할 단계: 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속함
2. 병합 단계: 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

## 병합 정렬 알고리즘

### 분할 과정의 알고리즘

~~~python
def merge_sort(m):
    if len(m) <= 1:
        return m
    
    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 2. CONQUER 부분: 분할된 리스트를 병합
    return merge(left, right)
~~~

### 병합 과정

~~~python
def merge(left, right):
    result = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result
~~~

| 알고리즘    | 평균 수행시간   | 최악 수행시간    | 알고리즘 기법 | 비고                                           |
| ----------- | --------------- | ---------------- | ------------- | ---------------------------------------------- |
| 버블 정렬   | $$O(n^2)$$      | $$O(n^2)$$       | 비교와 교환   | 코딩이 가장 손쉬움                             |
| 카운팅 정렬 | $$O(n+k)$$      | $$O(n + k)$$     | 비교환 방식   | n이 비교적 작을 때만 가능함                    |
| 선택 정렬   | $$O(n^2)$$      | $$O(n^2)$$       | 비교와 교환   | 교환의 회수가 버블, 삽입정렬보다 작음          |
| 퀵 정렬     | $$O(n log n)$$  | $$O(n^2)$$       | 분할 정복     | 최악의 경우 $$$$이지만, 평균적으로는 가장 빠름 |
| 삽입 정렬   | $$O(n^2)$$      | $$O(n^2) $$      | 비교와 교환   | n의 개수가 작을 때 효과적임                    |
| 병합 정렬   | $$O(n log n) $$ | $$O(n log n)  $$ | 분할 정복     | 연결 List의 경우 가장 효율적인 방식            |













