# BFS(너비 우선 탐색) 특징

## BFS(너비 우선 탐색) 특징

- 그래프 탐색 방법

  | DFS(Depth First Search, 깊이 우선 탐색 | BFS(breadth First Search, 너비 우선 탐색)                    |
  | -------------------------------------- | ------------------------------------------------------------ |
  | Stack 활용                             | 큐 활용                                                      |
  |                                        | 시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 장점들을 차례로 방문하는 방식 |
  |                                        | 인접한 정점들을 탐색한 후, 차례로 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용 |

## BFS(너비 우선 탐색) 알고리즘

- 입력 파라미터: 그래프 G와 탐색 시작점 v

  ~~~python
  def BFS(G, v):
      visited = [0] * n
      queue = []
      queue.append(v)
      while queue:
          t = queue.pop(0)
          if not visited[t]:
              visitied[t] = True
              visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
  ~~~

  



