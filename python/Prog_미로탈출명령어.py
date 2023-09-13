import sys
from collections import defaultdict
sys.setrecursionlimit(3000)

R = 0
C = 0
sr = 0
sc = 0
er = 0
ec = 0
K = 0
ans = ""
visited = [[]]


dr = [1,0,0,-1]
dc = [0,-1,1,0]
m = "dlru"

def in_range(r,c) :
    return 0<r<=R and 0<c<=C

def dfs(r,c, tmp) :
    global ans
    if visited[r][c][len(tmp)] :
        return False
    visited[r][c][len(tmp)] = True
    
    if len(tmp) == K :
        if r == er and c == ec : 
            ans = tmp
            return True
        return False
    
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if not in_range(nr,nc) : continue
        if dfs(nr,nc, tmp+m[i]) :
            return True
        
    return False
            

def solution(n, m, x, y, r, c, k):
    global R,C, sr,sc, er,ec, K, visited
    R = n
    C = m
    sr = x
    sc = y
    er = r
    ec = c
    K = k
    visited = [ [defaultdict(bool) for _ in range(C+1)] for _ in range(R+1) ]
    
    if dfs(sr,sc, "") :
        return ans
    return "impossible"

print(solution(3,3,0,0,2,0,3))