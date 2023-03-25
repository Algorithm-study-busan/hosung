from queue import PriorityQueue

edges = [
    [],
    [(2,3), (3,6), (4,7)],
    [(1,3), (3,1)],
    [(1,6), (2,1), (4,1)],
    [(1,7), (3,1)],
]

dist = [ 987654321 for _ in range(5)]

def dijkstra(s) :
    pq = PriorityQueue()
    pq.put((0,s))
    dist[s] = 0
    
    while not pq.empty() :
        cur_dist, cur_node = pq.get()
        if dist[cur_node] < cur_dist : continue
        
        for next_node, d in edges[cur_node] :
            next_dist = cur_dist + d
            if dist[next_node] > next_dist :
                dist[next_node] = next_dist
                pq.put((next_dist, next_node))
            
        
    
dijkstra(1)

print(dist)