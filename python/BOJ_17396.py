import heapq

N,M = map(int, input().split())
showed = list(map(int, input().split()))
edges = [[] for _ in range(N)]

for _ in range(M) :
    a,b,c = map(int, input().split())
    edges[a].append([b,c])
    edges[b].append([a,c])
    
pq = [[0,0]]
INF = 987654321000
dist = [INF for _ in range(N)]

while pq :
    cur_dist, cur_node = heapq.heappop(pq)
    if cur_dist > dist[cur_node] : continue
    
    for nxt_node, d in edges[cur_node] :
        nxt_dist = cur_dist + d
        if nxt_node != N-1 and showed[nxt_node] : continue
        
        if dist[nxt_node] > nxt_dist :
            dist[nxt_node] = nxt_dist
            heapq.heappush(pq, [nxt_dist, nxt_node])
            
            
print(-1 if dist[N-1] == INF else dist[N-1]) 
    
    