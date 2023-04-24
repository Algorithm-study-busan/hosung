import sys
input = sys.stdin.readline

def check_row(r, n):
  for i in range(9):
    if n == board[r][i]:
      return False
  return True

def check_column(c, n):
  for i in range(9):
    if n == board[i][c]:
      return False
  return True

def check_box(r, c, n):
  r_start, c_start = r // 3 * 3, c // 3 * 3
  for i in range(r_start, r_start + 3):
    for j in range(c_start, c_start + 3):
      if n == board[i][j]:
        return False
  return True

def f(idx):
  if idx == 81 : return True
  r = idx // 9
  c = idx % 9
  if board[r][c] != 0 : return f(idx+1)

  for i in range(1, 10):
    if check_row(r, i) and check_column(c, i) and check_box(r, c, i):
      board[r][c] = i
      if f(idx + 1) : return True
      board[r][c] = 0
  return False

board = []
for _ in range(9):
  board.append(list(map(int, input().split())))

f(0)

for b in board :
    print(*b)