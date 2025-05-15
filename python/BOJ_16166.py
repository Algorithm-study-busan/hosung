from collections import deque

N = int(input())

arr = []
for _ in range(N) :
    a = list(map(int, input().split()))
    arr.append(set(a[1:]))
E = int(input())


edges = [[] for _ in range(N)]

starts = []
ends = []
for i, node in enumerate(arr) :
    for n in node :
        if n == 0 : starts.append(i)
        if n == E : ends.append(i)
        for j, other_node in enumerate(arr) :
            if n in other_node :
                edges[i].append(j)

def bfs() :
    q = deque(starts)
    visited = [-1 for _ in range(N)]
    for start in starts :
        visited[start] = 0

    while q :
        cur = q.popleft()
        if cur in ends :
            print(visited[cur])
            return
        for nxt in edges[cur] :
            if visited[nxt] == -1 :
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

    print(-1)

bfs()

