from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

INF = 987654321

cube = []
for _ in range(5) :
    one = []
    for _ in range(5) :
        one.append(list(map(int, input().split())))
    cube.append(one)
    
dk = [-1,1,0,0,0,0]
dr = [0,0,-1,0,1,0]
dc = [0,0,0,1,0,-1]
ans = INF

def in_range(k, r, c) :
    return 0<=k<5 and 0<=r<5 and 0<=c<5 

def bfs(cube) :
    if cube[0][0][0] == 0 : return INF
    
    visited = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    q = deque([[0,0,0]])
    visited[0][0][0] = 0
    
    while q :
        ck, cr, cc = q.popleft()
        if ck == 4 and cr == 4 and cc == 4 :
            return visited[ck][cr][cc]
        for i in range(6) :
            nk = ck + dk[i]
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if not in_range(nk, nr, nc) or cube[nk][nr][nc] == 0 or visited[nk][nr][nc] != -1 : continue
            q.append([nk, nr, nc])
            visited[nk][nr][nc] = visited[ck][cr][cc] + 1
            
    return INF
    
def dfs(cube, k) :
    global ans
    if k == 5 : 
        for c in permutations(cube) :
            ans = min(ans, bfs(c))
        return
    
    for _ in range(4) :
        dfs(cube,k+1)
        rotate(cube, k)
        
        
def rotate(cube, k) :
    rotated = [[0 for _ in range(5)] for _ in range(5)]
    for r in range(5) :
        for c in range(5) :
            rotated[r][c] = cube[k][4-c][r]
    cube[k] = rotated
    
    
dfs(cube, 0)
print(-1 if ans == INF else ans)

