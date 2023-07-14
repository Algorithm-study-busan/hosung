from collections import deque

R = 0
C = 0
maps = [[]]
dr = [-1,0,1,0]
dc = [0,-1,0,1]

def in_range(r,c) :
    return 0<=r<R and 0<=c<C

def bfs(sr,sc, finish) :
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    visited[sr][sc] = 0
    q = deque([(sr,sc)])
    
    while q :
        cr,cc = q.popleft()
        
        if maps[cr][cc] == finish :
            return visited[cr][cc]
        
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if (not in_range(nr,nc) or
                maps[nr][nc] == 'X' or
                visited[nr][nc] >= 0) : continue
            
            visited[nr][nc] = visited[cr][cc]+1
            q.append((nr,nc))
            
    return -1
    
            
    

def solution(m):
    global R,C,maps
    maps = m
    R = len(maps)
    C = len(maps[0])
    
    sr = -1
    sc = -1
    lr = -1
    lc = -1
    
    for r in range(R) :
        for c in range(C) :
            if maps[r][c] == 'S' :
                sr = r
                sc = c
            if maps[r][c] == 'L' :
                lr = r
                lc = c
    
    to_L = bfs(sr,sc,'L')
    to_E = bfs(lr,lc,'E')
    
    return -1 if to_L == -1 or to_E == -1 else to_L + to_E

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))