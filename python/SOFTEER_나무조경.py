import sys

N = int(input())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))

ans = 0
def dfs(i, checked, tmp, k) :
    global ans
    ans = max(ans, tmp)
    
    if i == N*N or k == 4 : return
        
    r = i // N
    c = i % N
    if checked[r][c] :
        dfs(i+1, checked, tmp, k)
        return

    if c+1 < N and not checked[r][c+1] :
        checked[r][c] = True
        checked[r][c+1] = True
        dfs(i+1, checked, tmp + board[r][c] + board[r][c+1], k+1)
        checked[r][c] = False
        checked[r][c+1] = False
    if r+1 < N :
        checked[r][c] = True
        checked[r+1][c] = True
        dfs(i+1, checked, tmp + board[r][c] + board[r+1][c], k+1)
        checked[r][c] = False
        checked[r+1][c] = False
    dfs(i+1, checked, tmp, k)

checked = [[False] * N for _ in range(N)]
dfs(0, checked, 0, 0)
print(ans)
        
    