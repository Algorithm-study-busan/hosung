import sys
sys.setrecursionlimit(1000000)
from collections import deque

R,C = map(int, input().split())
dr = [-1,0,1,0]
dc = [0,-1,0,1]

board = []
for _ in range(R) :
    board.append(input())
    
ans = 0

def in_range(r,c) :
    if r<0 or r>=R or c<0 or c>=C : return False
    return True
    
def dfs(r,c, path) :
    global ans
    if board[r][c] in path : return
    path.append(board[r][c])
    ans = max(ans, len(path)) 
    for i in range(4) :
        nr = r+dr[i]
        nc = c+dc[i]
        if not in_range(nr,nc) : continue
        dfs(nr,nc,path)
    path.pop(-1)
        
dfs(0,0,[])

print(ans)