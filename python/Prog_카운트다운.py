from collections import deque
INF = 987654321
MAX = 100_000

visited = [[INF, INF] for _ in range(MAX+1)]

def move(nn, ncnt, nscore, q) :
    if nn > MAX : return
    if visited[nn][0] > ncnt or (visited[nn][0] == ncnt and visited[nn][1] < nscore): 
        visited[nn] = [ncnt, nscore]  
        q.append([nn, ncnt, nscore])
    

def bfs() :
    q = deque([[0,0,0]])
    visited[0] = [0,0]
    
    while q :
        n, cnt, score = q.popleft()
        
        for k in range(1,21) :
            move(n+k, cnt+1, score+1, q)
        
        for k in range(2,41,2) :
            move(n+k, cnt+1, score, q)
            
        for k in range(3,61,3) :
            move(n+k, cnt+1, score, q)
    
        move(n+50, cnt+1, score+1, q)
    

def solution(target):
    bfs()
    return visited[target]


print(solution(100_000))