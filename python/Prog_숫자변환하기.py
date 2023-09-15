from collections import deque

MAX = 1_000_001
visited = [-1 for _ in range(MAX)]
n = 0

def plus_n(x) :
    return x + n
def mul_2(x) :
    return x*2 
def mul_3(x) :
    return x*3

funcs = [plus_n, mul_2, mul_3]

def bfs(x,y,n) :
    q = deque([x])
    visited[x] = 0
    
    while q :
        cur = q.popleft()
        if cur == y :
            return visited[cur]
        for func in funcs :
            nxt = func(cur)
            if nxt >= MAX or visited[nxt]>=0 : continue
            visited[nxt] = visited[cur]+1
            q.append(nxt)
        
    return -1

def solution(x, y, nn):
    global n
    n = nn
    return bfs(x,y,n)