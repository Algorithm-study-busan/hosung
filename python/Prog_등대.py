N = 0
edges = [[]]

def solution(n, lighthouse):
    N = n
    edges = [[] for _ in range(N+1)]
    for a,b in lighthouse :
        edges[a].append(b)
        edges[b].append(a)