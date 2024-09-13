def solution(arrows):
    visited = set()
    edges = set()
    
    r, c = (0,0)
    visited.add((r,c))
    
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    
    def xEdge(r,c,nr,nc,d) :
        if d == 1 or d == 3 :
            return (r,c+1, nr,nc-1)
        elif d == 5 or d == 7 :
            return (r,c-1, nr,nc+1)
    
    ans = 0
    for d in arrows :
        nr = r + dr[d]
        nc = c + dc[d]
        
        if (nr,nc) in visited and (r,c,nr,nc) not in edges :
            ans += 1
        if d in (1,3,5,7) and (r,c,nr,nc) not in edges and xEdge(r,c, nr,nc, d) in edges :
            ans += 1
        
        visited.add((nr,nc))
        edges.add((r,c,nr,nc))
        edges.add((nr,nc,r,c))
        r = nr
        c = nc
    
    return ans