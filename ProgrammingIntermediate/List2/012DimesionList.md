# 2차원 리스트

## 2차원 List 구조

## List 초기화

1. `[0, 0, 0, 0, 0]`
2. `[0] * 5`
3. `[i for i in range(2, 9) if i % 0 == 0]`
4. `[[1, 2, 3], [1, 2, 3], [1, 2, 3]]`
5. `[[1, 2, 3]] * 3`
6. `[[1, 2, 3] for i in range(3)]` 

## 2차원 List 입력 받기

1. ~~~python
   n, m = map(int, input().split())
   mylist = [0 for _ in range(n)]
   
   for i in range(n):
   	mylist[i] = list(map(int, input().split()))
   ~~~

2. ~~~python
   n, m = map(int, input().split())
   mylist = []
   for i in range(n):
       mylist.append(list(map(int, input().split())))
   ~~~

3. ~~~python
   n, m = map(int, input().split())
   mylist = [list(map(int, input().split())) for _ in range(n)]
   ~~~

## 2차원 List에서 데이터의 위치 찾기

1. ~~~python
   n, m = map(int, input().split())
   newlist = []
   mylist = [0 for _ in range(n)]
   for i in range(n):
       mylist[i] = list(map(int, input().split()))
       for j in range(m):
           if mylist[i][j] == 1:
               newlist.append([i, j])
   ~~~

2. ~~~python
   n, m = map(int, input().split())
   mylist = [list(map(int, input().split())) for _ in range(n)]
   newlist = [(i, j) for i in range(n) for j in range(m) if mylist[i][j] == 1]
   ~~~

## 2차원 List의 순회

1. 행 우선 순회

2. 열 우선 순회

3. 지그재그 순회

   ~~~python
   n, m = len(arr), len(arr[0])
   for i in range(len(arr)):
       for j in range(len(arr[0])):
           arr[i][j + (m - 1 - 2 * j) * (i % 2)]
   ~~~

## 델타를 이용한 2차 List 탐색

1. 2차 List의 한 좌표에서 네 방향의 인접 List 요소를 탐색할 때 사용하는 방법
2. 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 List로 구현
3. 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음

~~~python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if not 0 <= testX < n: continue
            if not 0 <= testY < n: continue
            print(arr[testX][testY])
~~~



## 전치 행렬

~~~python
for i in range(arr):
    for j in range(arr):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
~~~



~~~python
arr = list(zip(arr))
~~~

