from collections import deque

N,K = map(int, input().split())

q = deque()

for n in range(1, N+1) :
    q.append(n)
    
ans = []

while q :
    for _ in range(K-1) :
        q.append(q.popleft())
    ans.append(str(q.popleft()))
    
print(f"<{', '.join(ans)}>")