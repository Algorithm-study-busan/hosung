from collections import deque

MAX = 1_000_001

def solution(arr):
    in_degree = [0 for _ in range(MAX)]
    edges = [[] for _ in range(MAX)]
    
    for a,b in arr :
        edges[a].append(b)
        in_degree[b] += 1
    
    node = -1
    for n in range(MAX) :
        if in_degree[n] == 0 and len(edges[n]) >= 2 :
            node = n
            break
        
    ans = [node,0,0,0]
    
    visited = [False for _ in range(MAX)]
    for s in edges[node] :
        q = deque([s])
        
        visited[s] = True
        is_cycle = False
        is_multi_edge = False
        
        while q :
            cur = q.popleft()
            
            if len(edges[cur]) > 1 : 
                is_multi_edge = True
                break
            
            for next in edges[cur] : 
                if visited[next] :  
                    is_cycle = True
                    continue
                
                visited[next] = True
                q.append(next)
        
        if is_multi_edge :
            ans[3] += 1
        elif is_cycle :
            ans[1] += 1
        else :
            ans[2] += 1
        
    return ans
    
    