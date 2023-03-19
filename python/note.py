# 각각의 경우가 독립적으로 이루어지기 때문에 visited 처리를 하지 않는다.
def bfs():
  global count
  # 같은 상황은 제외시키기 위해 집합 사용한다.
  q = set([(0, 0, board[0][0])])

  while q:
    # set 에서 pop 함수는 맨 앞의 요소를 삭제(반환)한다.
    a, b, s = q.pop()
    count = max(count, len(s))

    for i in range(4):
      if a + dr[i] < r and b + dc[i] < c and a + dr[i] >= 0 and b + dc[i] >= 0:
        nr = a + dr[i]
        nc = b + dc[i]
        if board[nr][nc] not in s:
          q.add((nr, nc, s + board[nr][nc]))

r, c = map(int, input().split())
board = []
for _ in range(r):
  board.append(list(input()))

dr = [0, 1, 0, -1]
dc = [1, 0 , -1, 0]

count = 1

bfs()
print(count)

