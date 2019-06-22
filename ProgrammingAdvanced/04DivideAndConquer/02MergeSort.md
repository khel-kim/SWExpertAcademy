# 병합 정렬

## 소개

- 병합 정렬
  - 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
  - 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후, 차례대로 정렬하여 최종 결과 획득
  - Top-down 방식
  - 시간복잡도
    - $$O(nlogn)$$

## 분할 정복

병합 정렬 과정

## 분할 알고리즘 

### 알고리즘: 분할 과정

~~~python
def merge_sort(m):
    if len(m) <= 1:
        return m
    
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
~~~

### 알고리즘: 병합 과정

리스트나 연결 리스트 자료구조를 이용하여 구현

- 리스트를 사용할 경우
  - 분리, 병합하는 과정에서 자료의 비교 연산과 이동 연산이 발생하여 비효율적
- 연결 리스트를 사용할 경우
  - 리스트를 사용할 경우의 비효율적 단점을 극복하여 효과적 구현 가능

~~~python
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if len[0] < = right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extent(right)
    return result
~~~



