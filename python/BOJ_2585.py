from collections import deque, defaultdict
import math

n,k = map(int, input().split())

pq = []

arr = []

for _ in range(n) :
    a,b = map(int, input().split())
    arr.append([a,b])

arr.append([0,0])
arr.append([10000,10000])

def cal(p1, p2) :
    return math.ceil(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5 / 10)

def bfs(oil) :
    q = deque([])
    q.append([n,  0])
    
    visited = [False for _ in range(n+2)]
    
    while q :
        cn, ck = q.popleft()
        if cn == n+1 : return True
        if ck > k : continue
        
        
        for nn in range(n+2) :
            if cn == nn : continue
            d = cal(arr[cn], arr[nn])
            if d > oil or visited[nn] : continue
            visited[nn] = True
            q.append([nn, ck+1])
            
    return False
    
lo = 0
hi = 987654321

while lo <= hi :
    mid = (lo+hi)//2
    
    if bfs(mid) : hi = mid-1
    else : lo = mid+1
            
print(lo)
