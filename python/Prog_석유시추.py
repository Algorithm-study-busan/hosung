from collections import deque

dr = [-1,0,1,0]
dc = [0,-1,0,1]

R = 0
C = 0
land = [[]]


def bfs(r,c, visited, oil_cnt) :
    q = deque([[r,c]])
    visited[r][c] = True
    cnt = 1 
    
    c_set = set()
    
    while q :
        cr,cc = q.popleft()
        c_set.add(cc)
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and land[nr][nc] == 1:
                visited[nr][nc] = True
                q.append([nr,nc])
                cnt += 1
                
    for c in c_set :
        oil_cnt[c] += cnt
    

def solution(land_):
    global R,C,land
    land = land_
    R = len(land)
    C = len(land[0])
    
    oil_cnt = [0 for _ in range(C)]
    
    visited = [[False for _ in range(C)] for _ in range(R)] 
    
    for r in range(R) :
        for c in range(C) :
            if not visited[r][c] and land[r][c] == 1: 
                bfs(r,c, visited, oil_cnt)
    
    return max(oil_cnt)


