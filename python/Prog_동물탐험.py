import sys
sys.setrecursionlimit(100000000)

def solution(n, path, order):
    edges = [[] for _ in range(200000)]
    
    for a,b in path :
        edges[a].append(b)
        edges[b].append(a)
    
    need = dict()
    for a,b in order :
        need[b] = a
        
    visited = set()
    can_go = dict()
    
    def dfs(cur) :
        if cur in need and need[cur] not in visited :
            can_go[need[cur]] = cur
            return
        
        visited.add(cur)
        for nxt in edges[cur] :
            if nxt in visited : continue
            dfs(nxt)
            
        if cur in can_go :
            dfs(can_go[cur])
    
    dfs(0)
    return len(visited) == n
    