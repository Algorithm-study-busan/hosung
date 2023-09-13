from collections import deque

MAX = 100
edges = [[] for _ in range(MAX+1)]

def bfs(a, b) :
    visited = [False for _ in range(MAX+1)]
    q = deque([a])
    visited[a] = True
    ret = 1
    
    while q :
        cur_node = q.popleft()
        for next_node in edges[cur_node] :
            if visited[next_node] or next_node == b : continue
            q.append(next_node)
            visited[next_node] = True
            ret += 1
            
    return ret
    
    

def solution(n, wires):
    ans = 987654321
    for a, b in wires :
        edges[a].append(b)
        edges[b].append(a)
        
    for a, b in wires :
        ans = min(ans, abs(bfs(a,b) - bfs(b,a)))
    return ans