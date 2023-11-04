from collections import deque
R = 0
C = 0

move = ['d', 'l', 'r', 'u']
dr = [1,0,0,-1]
dc = [0,-1,1,0]

def bfs(sr, sc, er, ec, k) :
    q = deque([[sr,sc, ""]])
    while q :
        cr, cc, cpath = q.popleft()
        print(cr,cc,cpath)
        
        if cr == er and cc == ec and len(cpath) == k :
            return cpath
        
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<R and 0<=nc<C :
                npath = cpath + move[i]
                if len(npath) > k : continue
                q.append([nr, nc, npath])
                
    return "impossible"

def solution(n, m, x, y, r, c, k):
    global R,C
    R = n
    C = m
    return bfs(x-1,y-1,r-1,c-1,k)

print(solution(3,4,2,3,3,1,5))