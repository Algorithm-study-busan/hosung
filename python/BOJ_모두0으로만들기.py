import sys
sys.setrecursionlimit(1_000_000)

edges = [[] for _ in range(300_001)]
weight = []
ans = 0

def dfs(parent, cur) :
    global ans
    ret = weight[cur]
    for nxt in edges[cur] :
        if parent == nxt : continue 
        x = dfs(cur, nxt)
        ret += x
        ans += abs(x)
    return ret

def solution(a_, edges_):
    global edges, weight
    weight = a_
    for a,b in edges_ :
        edges[a].append(b)
        edges[b].append(a)
    sum_a = dfs(-1, 0)
    if sum_a != 0 : return -1
    return ans
    
    