import heapq

MAX = 50_000
INF = 987654321

edges = [[] for _ in range(MAX+1)]
is_gate = [False for _ in range(MAX+1)]
is_summit = [False for _ in range(MAX+1)]

def dijkstra(gates) :
    dist = [INF for _ in range(MAX+1)]
    pq = []
    for g in gates :
        heapq.heappush(pq, [0,g])
        dist[g] = 0
    
    ret = [0, INF]

    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        
        if ret[0] != 0 and ret[1] < cur_dist : return ret
        
        if is_summit[cur_node] : 
            if ret[1] > cur_dist : 
                ret = [cur_node, cur_dist]
            elif ret[1] == cur_dist :
                ret[0] = min(ret[0], cur_node)
            continue
        
        for next_node, k in edges[cur_node] :
            next_dist = max(cur_dist, k)
            if dist[next_node] <= next_dist or is_gate[next_node] : continue
            dist[next_node] = next_dist
            heapq.heappush(pq, [next_dist, next_node])
            
    return ret
        
    
    

def solution(n, paths, gates, summits):
    for a,b,d in paths :
        edges[a].append([b,d])
        edges[b].append([a,d])
    
    for a in gates :
        is_gate[a] = True
        
    for a in summits :
        is_summit[a] = True
        
    summits.sort()
        
    return dijkstra(gates)
        
    
        