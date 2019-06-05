# 정렬

## 셀렉션 알고리즘

셀렉션 알고리즘: 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함

1. 정렬 알고리즘을 이용하여 자료를 정렬
2. 원하는 순서에 있는 원소 가져오기

k번쨰로 작은 원소를 찾는 알고리즘

~~~python
def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k - 1]
~~~

## 선택 정렬

선택 정렬 의미: 주어진 자료들 중 가장 작은 갑스이 원소부터 차례대로 선택하여 위치를 교환하는 방식

셀렉션 알고리즘을 전체 자료에 적용한 것

1. 주어진 List 중에서 최소값을 찾음
2. 그 값을 List의 맨 앞에 위치한 값과 교환
3. 맨 처음 위치를 제외한 나머지 List를 대상으로 위의 과정을 반복

시간 복잡도: $$O(N^2)$$ 