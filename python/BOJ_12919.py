from collections import defaultdict

start = input()
end = input() 

visited = defaultdict(bool)

def bfs() :
    q = [end]
    visited[end] = True
    
    while q : 
        cur = q[0]
        q.pop(0)
        
        if len(cur) < len(start) : continue
        
        if cur[-1] == 'A' :
            nxt = cur[:-1]
            if visited[nxt] : continue
            visited[nxt] = True
            q.append(nxt)
        if cur[0] == 'B' :
            nxt = cur[::-1][:-1]
            if visited[nxt] : continue
            visited[nxt] = True
            q.append(nxt)
            
            
bfs()
print(1 if visited[start] else 0)
        
        