# 분할 정복 기법

## 소개

### 가짜 동전 찾기

- n개의 동전들 중에 가짜 동전이 하나 포함되어 있음
  - 가짜 동전은 진짜 동전에 비해 아주 조금 가벼움
- 진짜 동전들의 무게가 동일하다고 할 때 양팔 저울을 이용해서 가짜 동전 찾아보기
- 양팔 저울을 최소로 사용해서 가짜 동전을 찾는 방법은 무엇인가?
  - 동전을 하나씩 올려 놓고 무게를 재기
  - 양팔 저울을 평균 6번 사용해야 함
  - 어떤 식으로 양팔 저울을 사용해야 사용 횟수를 최소로 할 수 있을까?

### 분할 정복 알고리즘의 유래

나폴레이옹이 사용한 전략

### 분할 정복 알고리즘의 설계 전략

분할(Divide)

- 해결할 문제를 여러 개의 작은 부분 문제들로 분할

정복(Conquer)

- 나눈 작은 문제를 각각 해결

통합(Combine)

- 필요 시 해결된 해답을 모음

Top-down approach

- 문제의 크기 n
  - 분할, 크기 n / 2인 부분문제 1
    - 부분 문제1의 해
  - 분할, 크기 n / 2인 부분문제 2
    - 부분 문제2의 해
  - 전체 문제의 해

## 거듭제곱

### 반복(iterative) 알고리즘: O(n)

- C의 거듭제곱 = 1에 거듭제곱 값만큼 C를 곱하는 방법으로 연산 수행

  ~~~python
  def iterative_Power(C, n):
      result = 1
      for _ in range(n):
          result = result * C
      return result
  ~~~

### 분할 정복 기반의 알고리즘: $$O(log_2 n)$$

~~~python
def Recursive_Power(C, n):
    if n == 1:
        return C
    if n % 2 == 0:
        y = Recursive_Power(C, n / 2)
        return y * y
    else:
        y = Recursive_Power(C, (n-1)/2)
        return y * y * C
~~~

