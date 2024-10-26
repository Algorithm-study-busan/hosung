from collections import deque

def solution(n, e):
    edges = [[] for _ in range(250_001)]
    
    for a,b in e :
        edges[a].append(b)
        edges[b].append(a)
        
    def bfs(start) :
        q = deque([[start, 0]])
        visited = [False for _ in range(250_001)]
        visited[start] = True
        
        max_dist = -1
        ret = []
        while q :
            cur_node, cur_dist = q.popleft()
            if cur_dist > max_dist :
                max_dist = cur_dist
                ret = [cur_node]
            elif cur_dist == max_dist :
                ret.append(cur_node)
                
            for nxt_node in edges[cur_node] :
                if visited[nxt_node] : continue
                visited[nxt_node] = True
                q.append([nxt_node, cur_dist+1])
                
        return ret, max_dist
    
    node_arr, dist = bfs(1)
    pair_set = set()
    for pair_node in node_arr :
        pair_node_arr, pair_dist = bfs(pair_node)
        if len(pair_node_arr) > 1 : return pair_dist
        for p1 in node_arr :
            for p2 in pair_node_arr :
                if (p1,p2) in pair_set or (p2,p1) in pair_set : continue
                pair_set.add((p1,p2))
                
    if len(pair_set) > 1 : return pair_dist
    return pair_dist-1
        