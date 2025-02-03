import sys
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

signal = [
    {},
    [0,1,2],
    [3,0,1],
    [2,3,0], 
    [1,2,3],
    [0,1],
    [3,0],
    [2,3],
    [1,2],
    [2,1],
    [1,0],
    [0,3],
    [3,2]
]

N, T = map(int, input().split())
board = []

for i in range(N) :
    row = []
    for j in range(N) :
        row.append(list(map(int, input().split())))
    board.append(row)

visited =[ [ [ [False]*4 for _ in range(4) ] for _ in range(N) ] for _ in range(N)] 

q = deque([[0,0,0,0,0]])

ans = {0}

while q :
    cr, cc, cd, ct, total_t = q.popleft()
    if total_t >= T : continue
    sg = board[cr][cc][ct]
    if signal[sg][1] != cd : continue
    
    for nd in signal[sg] :
        nr = cr + dr[nd]
        nc = cc + dc[nd]
        nt = (ct+1)%4
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc][nd][nt] :
            visited[nr][nc][nd][nt] = True
            ans.add(nr*N + nc)
            q.append([nr,nc,nd,nt, total_t+1])
        
print(len(ans))