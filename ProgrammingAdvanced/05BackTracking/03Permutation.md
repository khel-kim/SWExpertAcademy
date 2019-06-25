# 순열

## 소개

### 순열에 대한 상태 공간 트리

- 노드 방문 시마다 저장 내용은 원소를 가리키는 인덱스 값 저장
- 같은 원소 수를 가지는 집합에 대해 부분집합과 순열의 상태 공간 트리 높이 같음
- 순열의 경우는 높이가 다른 노드들은 선택지의 수가 동일하지 않음
- 높이가 증가하면서 선택지의 수 하나씩 감소

## 알고리즘

### 모든 순열 생성 알고리즘

~~~python
def permutation(order, k, n):
    if k == n:
        print_order_array(order, n)
    else:
        check = [False] * n
        for i in range(k):
            check[order[i]] = True
        for i in range(n):
            if check[i] == False:
                order[k] = i
                permutation(order, k+1, n)
~~~

