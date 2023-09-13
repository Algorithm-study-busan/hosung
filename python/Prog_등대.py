import sys
sys.setrecursionlimit(1_000_000)

MAX = 100_000
edges = [[] for _ in range(MAX+1)]
dp = [[-1,-1] for _ in range(MAX+1)]

def dfs(cur_node, parent_node, parent_on) :
    if dp[cur_node][parent_on] != -1 : return dp[cur_node][parent_on]
    cur_on = 1
    for next_node in edges[cur_node] :
        if next_node == parent_node : continue
        cur_on += dfs(next_node, cur_node, True)
        
    cur_off = 0
    for next_node in edges[cur_node] :
        if next_node == parent_node : continue
        cur_off += dfs(next_node, cur_node, False)
    
    if parent_on :
        dp[cur_node][parent_on] = min(cur_on, cur_off)
    else :
        dp[cur_node][parent_on] = cur_on
        
    return dp[cur_node][parent_on]
        

def solution(n, lighthouse):
    global dp, edges
    for a,b in lighthouse :
        edges[a].append(b)
        edges[b].append(a)
        
    return dfs(1, -1, True)
    