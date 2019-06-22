# 이진 검색

## 소개

- 이진 검색
  - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행해 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행
  - 이진 검색을 위해서 자료 정렬 상태 필요

## 검색 방법

### 이진 검색의 검색 과정

1. 자료의 중앙에 있는 원소를 고른다
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값과 중앙 원소 값의 관계
   1. 목표 값 < 중앙 원소 값
      1. 자료의 왼쪽 반에 대해서 새로 검색 수행
   2. 목표 값 > 중앙 원소 값
      1. 자료의 오른쪽 반에 대해서 새로 검색 수행
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정 반복

## 알고리즘

### 알고리즘: 반복 구조

- 이진 검색의 경우
- 자료 삽입, 삭제 발생 시 리스트의 상태를 항상 정렬 상태로 유지하는 추가 작업 필요

~~~python
# a: 검색할 리스트
# key: 검색하고자 하는 값

def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1 
~~~

### 알고리즘: 재귀구조

~~~python
# a: 검색할 리스트
# key: 검색하고자 하는 값

def binarySearch2(a, low, high, key):
    if low > high:
        return -1
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        else:
            return binarySearch2(a, middle+1, high, key)
~~~

