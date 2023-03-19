import sys 
input=sys.stdin.readline

R,C = map(int, input().split())
dr = [-1,0,1,0]
dc = [0,-1,0,1]
visited = [False for _ in range(26)]

board = []
for _ in range(R) :
    board.append(input())
    
ans = 0

def in_range(r,c) :
    if r<0 or r>=R or c<0 or c>=C : return False
    return True
    
def dfs(r,c,cnt) :
    global ans
    x = ord(board[r][c])-65
    if visited[x] : return
    visited[x] = True
    ans = max(ans, cnt+1) 
    for i in range(4) :
        nr = r+dr[i]
        nc = c+dc[i]
        if not in_range(nr,nc) : continue
        dfs(nr,nc,cnt+1)
    visited[x] = False
        
dfs(0,0,0)

print(ans)