from sys import stdin
input = stdin.readline

from collections import deque

N = int(input())
edges = [[] for _ in range(N+1)]

for _ in range(N) :
    arr = list(map(int, input().split()))
    for i in range(1,len(arr)-1,2) :
        edges[arr[0]].append([arr[i], arr[i+1]])
    
def bfs(s) :
    q = deque([[s,0]])
    visited = [False for _ in range(N+1)]
    visited[s] = True
    
    node = -1
    dist = -1
    
    while q :
        cur_node, cur_dist = q.popleft()
        if cur_dist > dist : 
            node = cur_node
            dist = cur_dist
        for next_node, d in edges[cur_node] :
            next_dist = cur_dist + d
            if visited[next_node] : continue
            visited[next_node] = True
            q.append([next_node, next_dist])
            
    return node, dist

node,dist = bfs(1)
node,dist = bfs(node)
print(dist)
            
            
        
    