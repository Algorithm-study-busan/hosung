from collections import deque

dr = [-1,0,1,0]
dc = [0,-1,0,1]
N = 0

def in_range(r, c) :
    return 0 <= r < N and 0 <= c < N

def bfs(land, r,c, color, height, land_color) :
    land_color[r][c] = color
    q = deque()
    q.append((r,c))
    
    while q :
        cr, cc = q.popleft()
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if not in_range(nr,nc) or land_color[nr][nc] == color or abs(land[nr][nc] - land[cr][cc]) > height : continue
            land_color[nr][nc] = color
            q.append((nr,nc))
        

def coloring(land, height, land_color) :
    color = 1
    for r in range(N) :
        for c in range(N) :
            if land_color[r][c] != -1 : continue
            bfs(land, r, c, color, height, land_color)
            color += 1
            
            
def bfs_dist(land, land_color, dist, r,c, visited) :
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    
    while q : 
        cr, cc = q.popleft()
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if not in_range(nr,nc) or visited[nr][nc] : continue
            
            if land_color[nr][nc] != land_color[r][c] :
                dist.append((land_color[r][c], land_color[nr][nc], abs(land[nr][nc] - land[cr][cc])))
                continue
            
            visited[nr][nc] = True
            q.append((nr,nc))
                
            
def find_dist(land, land_color, dist) :
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    for r in range(N) :
        for c in range(N) :
            if visited[r][c] : continue
            bfs_dist(land, land_color, dist, r,c, visited)
            
def find_parent(a, parent) :
    if a == parent[a] : return a
    parent[a] = find_parent(parent[a], parent)
    return parent[a]

def union_node(a, b, parent) :
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    if a < b : parent[b] = a
    else : parent[a] = b
    
def is_set(a,b, parent) :
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    return a == b
    

def solution(land, height):
    global N, dr, dc
    N = len(land)
    land_color = [[-1 for _ in range(N)] for _ in range(N)]
    coloring(land, height, land_color)
    
    dist = []
    find_dist(land, land_color, dist)
    
    dist.sort(key=lambda x : x[2])
    parent = [i for i in range(N*N+1)]
    
    ans = 0
    for a,b,d in dist :
        if is_set(a,b, parent) : continue
        ans += d
        union_node(a,b, parent)
        
    return ans
    
    
    
    

    
