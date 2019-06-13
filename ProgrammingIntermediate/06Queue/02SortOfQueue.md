# Queue의 종류

## 선형 Queue

- 선형 큐의 특징

  1. 1차원 리스트를 이용한 큐
     - 큐의 크기 = 리스트의 크기
     - front: 저장된 첫 번째 원소의 인덱스
     - rear: 저장된 마지막 원소의 인덱스
  2. 상태 표현
     - 초기 상태: front = rear = -1
     - 공백 상태: front = rear
     - 포화 상태: rear = n - 1(n: 리스트의 크기, n - 1: 리스트의 마지막 인덱스)

- 선형 큐의 구현

  1. 초기, createQueue()

     1. 초기 공백큐 생성
        1. 크기 n인 1차원 리스트 생성
        2. front, rear = -1로 초기화

  2. enQueue(item)

     1. 삽입 enQueue(item)

        마지막 원소 뒤에 새로운 원소를 삽입하기 위해

        1. rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련함

        2. 그 인덱스에 해당하는 리스트원소 Q[rear]에 item을 저장

        3. ~~~python
           def enQueue(item):
               global rear
               if isFull(): print("Queue_FUll")
               else:
                   rear += 1
                   Q[rear] = item
           ~~~

  3. deQueue()

     1. 삭제: deQueue()

        가장 앞에 있는 원소를 삭제하기 위해

        1. front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동함

        2. 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능을 함

        3. ~~~python
           def deQueue():
               global front
               if isEmpty(): print("Queue_Empty")
               else:
                   front += 1
                   return Q[front]
           ~~~

  4. isEmpty(), isFull()

     1. 공백상태 및 포화상태 검사: isEmpty(), isFull()

        공백상태: front = rear

        포화상태: rear = n - 1

        (n: 리스트의 크기, n - 1: 리스트의 마지막 인덱스)

        ~~~python
        def isEmpty():
            return front == rear
        def isFull():
            return rear == len(Q) - 1
        ~~~

  5. Qpeek()

     1. 검색: Qpeek()

        가장 앞에 있는 원소를 검색하여 반환하는 연산

        현재 front의 한자리 뒤(front + 1) 에 있는 원소, 즉 큐의 첫 번쨰에 있는 원소를 반환

        ~~~python
        def Qpeek():
            if isEmpty(): print("Queue_Empty")
            else: return Q[front + 1]
        ~~~

- 선형 큐의 문제점: 잘못된 포화 상태 인식

  - 리스트의 크기를 고정 -> 사용할 큐의 크기만큼을 미리 확보 -> 메모리의 낭비 발생

  1. 삽입, 삭제를 계속할 경우 리스트의 앞부분에 활용할 수 있는 공간이 있음에도, rear = n - 1인 상태 즉, 포화 상태로 인식
  2. 더 이상의 삽입을 수행할 수 없음

| 선형 큐의 장점             | 선형 큐의 단점     |
| -------------------------- | ------------------ |
| 삽입, 삭제의 처리속도 빠름 | 메모리 낭비가 심함 |

- 선형 큐의 단점 해결 방법
  - 원형 큐 사용으로 메모리 절약
  - 파이썬의 리스트 특성을 사용한 큐 사용으로 메모리 절약
    - 단점: 삽입, 삭제 시 복사, 데이터 이동시키는 연산 수행에 많은 시간 소모
  - 단순연결 리스트로 구현한 큐 사용으로 메모리 동적 확보
  - 큐 라이브러리 사용

## 원형 Queue

- 원형 큐

  - 1차원 리스트를 사용하되, 논리적으로 리스트의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용함

- 원형 큐의 특징

  1. 초기 공백 상태

     1. front = rear = 0

  2. Index의 순환

     1. front와 rear의 위치가 리스트이 마지막 인덱스인 n - 1를 가리킨 후, 논리적 순환을 이루어 리스트의 처음 인덱스인 0으로 이동해야 함
     2. 이를 위해 나머지 연산자 %를 이용

  3. front 변수

     1. 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

  4. 삽입 위치 및 삭제 위치

     1. .

        | 테이블 인덱스 | 삽입 위치             | 삭제 위치               |
        | ------------- | --------------------- | ----------------------- |
        | 선형 큐       | rear = rear + 1       | front = front + 1       |
        | 원형 큐       | rear = (rear + 1) % n | front = (front + 1) % n |

- 원형 큐의 기본 연산 과정

- 원형 큐의 구현

  1. 초기

     초기 공백큐 생성

     크기 n인 1차원 리스트 생성

  2. isEmpty(), isFull()

     공백상태 및 포화상태 검사: isEmpty(), isFull()

     공백상태: front = rear

     포화상태: 삽입할 rear의 다음 위치 = 현재 front

     (rear + 1) % n = front

     ~~~python
     def isEmpty():
         return front == rear
     def isFull():
         return (rear + 1) % len(cQ) == front 
     ~~~

  3. enQueue(item)

     삽입: enQueue(itme)

     마지막 원소 뒤에 새로운 원소 삽입하기 위해

     1. rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함: rear <- (rear + 1) % n;
     2. 인덱스에 해당하는 리스트원소 cQ[rear]에 item을 저장

     ~~~python
     def enQueue(item):
         global rear
         if isFull():
             print("Queue_Full")
         else:
             rear = (rear + 1) % len(cQ)
             cQ[rear] = item
     ~~~

  4. deQueue()

     삭제: deQueue(), delete()

     가장 앞에 있는 원소를 삭제하기 위해

     1. front 값을 조정하여 삭제할 자리를 준비함
     2. 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능을 함

     ~~~python
     def deQueue():
         global front
         if isEmpty():
             print("Queue_Empty")
         else:
             front = (front + 1) % len(cQ)
             return cQ[front]
     def delete():
         global front
         if isEmpty():
             print("Queue_Empty")
         else:
             front = (front + 1) % len(cQ)
     ~~~


## 리스트의 특성을 사용한 Queue

1. 파이썬의 리스트 특성을 사용한 큐

   - 리스트는 크기를 동적으로 변경할 수 있음
   - 메모리 절약
   - 삽입, 삭제 시 복사, 데이터를 이동시키는 연산을 수행하는데 많은 시간 소모

2. 리스트의 메서드

   | 메서드       | 설명                    |
   | ------------ | ----------------------- |
   | append(item) | 마지막 위치에 원소 추가 |
   | pop(index)   | index 위치에 원소 삭제  |

3. front는 리스트의 맨 앞: -1

4. rear는 리스트의 맨 뒤: len(queue) - 1

## 연결 Queue

- 연결 큐의 특징
  1. 단순 연결 리스트(Linked List)를 이용한 큐
     1. 큐의 원소: 단순 연결 리스트의 노드
     2. 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음
     3. front: 첫 번쨰 노드를 가리키는 링크
     4. rear: 마지막 노드를 가리키는 링크
  2. 상태 표현
     1. 초기 상태: front = rear = None
     2. 공백 상태: front = rear = None

- 연결 큐의 연산 과정

  1. 큐 생성

     createLinkedQueue():

     front = None

     rear = None

  2. 원소 A 삽입: enQueue(A)

     front = A 위치

     rear = A 위치

  3. 원소 B 삽입: enQueue(B)

     front = A 위치

     rear = B 위치

  4. 원소 삭제: deQueue():

     front = B 위치

     rear = B 위치

  5. 원소 삭제: deQueue():

     front = None

     rear = None

- 연결 큐의 구현

  1. createLinkedQueue():

     초기 공백 큐 생성: createLinkedQueue()

     리스트 노드 없이 포인터 변수만 생성함

     front와 rear를 None로 초기화

     ~~~python
     front = None
     rear = None
     ~~~

  2. isEmpty()

     공백상태 검사: isEmpty()

     공백상태: front = rear = None

     ~~~python
     def isEmpty():
         return front == None
     ~~~

  3. enQueu(item)

     삽입: enQueue(item)

     1. 새로운 노드 생성 후 데이터 필드에 item 저장
     2. 연결 큐가 공백인 경우, 아닌 경우에 따라 front, rear 변수 지정

     ~~~python
     def enQueue(item):
         global front, rear
         newNode = Node(item)
         if is Empty():
             front = newNode
         else:
             rear.next = newNode
         rear = newNode
     ~~~

  4. deQueue()

     삭제: deQueue()

     1. old가 지울 노드를 가리키게 하고, front 재설정
     2. 삭제 후 공백 큐가 되는 경우, rear도 None로 설정
     3. old가 가리키는 노드를 삭제하고 메모리 반환

     ~~~python
     def deQueue():
         global front, rear
         if isEnmpty():
             print("Queue_Empty")
             return None
         item = front.item
         front = front.next
         if isEmpty():
             rear = None
         return item
     ~~~

## Queue 라이브러리

- 큐 모듈

  1. 큐 모듈에 정의된 클래스

     | 클래스                       | 내용                                                         |
     | ---------------------------- | ------------------------------------------------------------ |
     | queue.Queue(maxsize)         | 선입선출(FIFO, first-In, First-Out) 큐 객체를 생성           |
     | queue.LifoQueue(maxsize)     | 스택(stack)개념의 후입선출 (LIFO, Last-In, First-Out) 큐 객체 생성 |
     | queue.PriorityQueue(maxsize) | 우선순위 큐 객체를 생성, 입력되는 아이템의 형식은 (순위, 아이템)의 튜플로 입력되며, 우선순위는 숫자가 작을수록 높은 순위를 가짐 |

  2. maxsize는 최대 아이템수, 지정하지 않거나 음수이면 내용만큼 늘어남

  3. 제시된 3개의 클래스는 다음과 같은 멧드를 동일하게 가짐

     | 메서드                        | 내용                                            |
     | ----------------------------- | ----------------------------------------------- |
     | qsize()                       | 큐 객체에 입력된 아이템의 개수를 반환           |
     | put(item[, block[, timeout]]) | 큐 객체에 아이템을 입력                         |
     | get([block[, timeout]])       | 생성된 큐 객체 특성에 맞추어, 아이템 1개를 반환 |
     | empty()                       | 큐객체가 비어있으면 True 리턴                   |
     | full()                        | 큐 객체가 꽉차있으면 True 리턴                  |

  4. 클래스의 정렬방식에 따라 get 계열의 메서드 결과가 달라짐

