from collections import deque

def solution(land, height):
    N = len(land)
    board = [[-1 for _ in range(N)] for _ in range(N)]
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    
    def bfs(n, r,c) :
        board[r][c] = n
        q = deque([[r,c]])
        while q :
            cr,cc = q.popleft()
            
            for i in range(4) :
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0<=nr<N and 0<=nc<N and board[nr][nc] == -1 and abs(land[nr][nc]-land[cr][cc]) <= height :
                    board[nr][nc] = n
                    q.append([nr,nc])
    
    num = 0
    for r in range(N) :
        for c in range(N) :
            if board[r][c] == -1 :
                bfs(num, r,c)
                num += 1
    
    arr = []
    for r in range(N) :
        for c in range(N) :
            if r < N-1 and board[r][c] != board[r+1][c] :
                arr.append([board[r][c], board[r+1][c], abs(land[r][c] - land[r+1][c])])
            if c < N-1 and board[r][c] != board[r][c+1] :
                arr.append([board[r][c], board[r][c+1], abs(land[r][c] - land[r][c+1])])
                
    arr.sort(key = lambda x : x[2])
    
    s = [i for i in range(num)]
    
    def getParent(n) :
        if s[n] == n : return n
        s[n] = getParent(s[n])
        return s[n]
    
    def union(a, b) :
        a = getParent(a)
        b = getParent(b)
        if a < b : s[b] = a
        else : s[a] = b
        
    ans = 0
    for a,b, d in arr :
        if getParent(a) != getParent(b) :
            union(a,b)
            ans += d
    return ans