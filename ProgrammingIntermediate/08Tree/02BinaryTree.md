# Binary Tree

## Binary Tree의 특징

### 이진 트리

1. 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
2. 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
   1. 왼쪽 자식 노드(Left child node)
   2. 오른쪽 자식 노드(Right child node)
3. 레벨 i에서의 노드의 최대 개수는 $$2^i$$개
4. 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 $$(h + 1)$$개, 최대 개수는 $$(2 ^ {h + 1} - 1)$$

## Binary Tree의 종류

- 포화 이진 트리(Full binary Tree)
- 완전 이진 트리(Complete binary Tree)
- 편향 이진 트리(Skewed binary Tree)

### 포화 이진 트리(Full binary Tree)

모든 레벨에 노드가 포화상태로 차 있는 이진 트리

1. 최대의 노드 개수인 $$(2 ^ {h + 1} - 1)$$의 노드를 가진 이진 트리
2. 루트를 1번으로 하여 $$2 ^ {h + 1} -1$$까지 정해진 위치에 대한 노드 번호를 가짐

### 완전 이진 트리(Complete binary Tree)

높이가 h이고 노드 수가 n개일 때(단, $$2^ h \leq n \leq 2 ^ {h + 1} - 1$$), Full 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

### 편향 이진 트리(Skewed binary Tree)

높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드 만을 가진 이진 트리(왼쪽 편향 이진 트리, 오른쪽 편향 이진 트리)

## Binary Tree - 순회(traversal)

### 순회(Traversal)

트리의 각 노드를 중복되지 않게 전부 방문(Visit) 하는 것을 말하는데, 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없음 -> 특별한 방법이 필요

### 3가지의 기본적인 순회방법

- 전위 순회(Preorder traversal)
  - 자손노드보다 루트노드를 먼저 방문
- 중위 순회(Inorder traversal)
  - 왼쪽 자손, 루트, 오른쪽 자손 순으로 방문
- 후위 순회(Postorder traversal)
  - 루트노드보다 자손을 먼저 방문

### 전위 순회(Preorder traversal)

수행 방법

1. 현재 노드 n을 방문하여 처리: V
2. 현재 노드 n의 왼쪽 서브트리로 이동: L
3. 현재 노드 n의 오른쪽 서브트리로 이동: R

~~~python
def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
~~~

### 중위 순회(Inorder traversal)

수행 방법

1. 현재 노드 n의 왼쪽 서브트리로 이동: L
2. 현재 노드 n을 방문하여 처리: V
3. 현재 노드 n의 오른쪽 서브트리로 이동: R

~~~python
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)
~~~

### 후위 순회(Postorder traversal)

1. 현재 노드 n의 왼쪽 서브트리로 이동: L
2. 현재 노드 n의 오른쪽 서브트리로 이동: R
3. 현재 노드 n을 방문하여 처리: V

~~~python
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)
~~~

### 이진 트리 순회방법 비교

- 프리오더(Preorder) 전위 순회
  - 각 정점 왼쪽
- 인오더(Inorder) 중위 순회
  - 각 정점 아래쪽
- 포스트오더(Postorder) 후위 순회
  - 각 정점 오른쪽

































