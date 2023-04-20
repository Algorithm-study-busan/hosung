from collections import deque

INF = 987654321

def bfs():
  q = deque()
  q.append((0, 0))
  count[0][0] = 0

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if nr < n and nc < m and nr >= 0 and nc >= 0:
        next_count = count[r][c] + (1 if board[nr][nc] == 1 else 0)
        if count[nr][nc] <= next_count : continue
        count[nr][nc] = next_count
        q.append((nr,nc))
          

m, n = map(int, input().split())
board = []
for _ in range(n):
  lst = list(input())
  board.append(list(map(int, lst)))

count = [[INF] * m for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

bfs()
print(count[n - 1][m - 1])