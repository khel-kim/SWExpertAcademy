# Memoization

## 피보나치 수열

재귀 호출을 작성할 수 있는 함수 - 피보나치 수열을 구하는 함수

1. 0과1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열
2. 피보나치 수열의 i번 째 값을 계산하는 함수 F를 정의하면 다음과 같음
   1. $$F_0 = 0, F_1 = 1$$
   2. $$F_i = F_(i-1) + F_(i-2)$$ for $$i \geq 2$$
3. 위의 정의로부터 피보나치 수열의 i번쨰 항을 반환하는 함수를 재귀 함수로 구현할 수 있음

## 피보나치 수를 구하는 재귀 함수

피보나치 수열을 구하는 함수의 알고리즘

~~~python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
~~~

하지만 이렇게 구현한 피보나치 수열을 구하는 함수는 엄청난 중복 호출이 존재함

## Memoization이란?

### 메모이제이션(Memoization)의 의미

1. 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
2. DP(동적계획법)의 핵심이 되는 기술

### Memoization 단어의 의미

1. 글자 그대로 해석하면 '메모리에 넣기(to put in memory)'라는 의미
2. '기억되어야 할 것'이라는 뜻의 라틴어 Memorandum에서 파생
3. 흔히 '기억하기', '암기하기'라는 뜨스이 Memorization과 혼동하지만, 정확한 단어는 Memoization으로 동사형은 memoize임

### Memoization 방법을 적용한 알고리즘

피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면 실행시간을 줄일 수 있음

만약 기존에 계산하여 저장된 값이 있을 경우에는 다시 계산하지 않겠다는 알고리즘

~~~python
# memo를 위한 리스트를 생성하고,
# memo[0]을 0으로 memo[1]은 1로 초기화 한다

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n - 1) + fibo1(n - 2))
    return memo[n]

memo = [0, 1]
~~~

