from collections import deque

R = 0
C = 0
maps = [[]]
dr = [-1,0,1,0]
dc = [0,-1,0,1]
visited = [[]]

def in_range(r,c) :
    return 0<=r<R and 0<=c<C

def bfs(r,c) :
    q = deque([(r,c)])
    visited[r][c] = True
    ret = int(maps[r][c])
    
    while q :
        cr,cc = q.popleft()
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if not in_range(nr,nc) or visited[nr][nc] or maps[nr][nc] == 'X': continue
            visited[nr][nc] = True
            q.append((nr,nc))
            ret += int(maps[nr][nc])
            
    return ret

def solution(m):
    global R,C,maps,visited
    maps = m
    R = len(maps)
    C = len(maps[0])
    visited = [[False for _ in range(C)] for _ in range(R)]
    answer = []
    
    for r in range(R) :
        for c in range(C) : 
            if maps[r][c] == 'X' or visited[r][c] : continue
            answer.append(bfs(r,c))
            
    answer.sort()
    
    return [-1] if len(answer) == 0 else answer