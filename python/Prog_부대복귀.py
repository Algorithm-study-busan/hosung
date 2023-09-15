from collections import deque

MAX = 100_000

edges = [[] for _ in range(MAX+1)]
dist = [-1 for _ in range(MAX+1)]

def bfs(s) :
    q = deque([s])
    dist[s] = 0
    while q :
        cur_node = q.popleft()
        for next_node in edges[cur_node] :
            if dist[next_node] != -1 : continue;
            dist[next_node] = dist[cur_node] + 1
            q.append(next_node)

def solution(n, roads, sources, destination):
    global edges, dist
    for a,b in roads :
        edges[a].append(b)
        edges[b].append(a)
    bfs(destination)
    ans = []
    for s in sources :
        ans.append(dist[s])
        
    return ans