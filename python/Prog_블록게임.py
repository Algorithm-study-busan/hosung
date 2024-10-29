from collections import deque

def solution(board):
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    N = len(board)
    
    def bfs(r,c, visited) :
        q = deque([[r,c]])
        
        sr = r
        sc = c
        er = r
        ec = c
        
        while q :
            cr,cc = q.popleft()
            for i in range(4) :
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and board[cr][cc] == board[nr][nc] :
                    visited[nr][nc] = True
                    q.append([nr,nc])
                    sr = min(sr, nr)
                    sc = min(sc, nc)
                    er = max(er, nr)
                    ec = max(ec, nc)
                    
        return sr,sc,er,ec
    
    def is_rectangle(num, sr,sc,er,ec) :
        if er-sr == 1 :
            if board[sr][sc+1] == 0 and board[sr][ec] == 0 : return True
            elif board[sr][sc] == 0 and board[sr][sc+1] == 0 : return True
            elif board[sr][sc] == 0 and board[sr][ec] == 0 : return True
            return False
        else :
            if board[sr][sc] == 0 and board[sr+1][sc] == 0 : return True
            if board[sr][ec] == 0 and board[sr+1][ec] == 0 : return True
            return False
                    
    def remove(num,sr,sc,er,ec) :
        for r in range(sr,er+1) :
            for c in range(sc, ec+1) :
                if board[r][c] == num : board[r][c] = 0
                
    def can_drop(sr,sc, er,ec) :
        for r in range(sr,er+1) :
            for c in range(sc, ec+1) :
                if board[r][c] == 0 and not can_drop_col(r,c) : return False
        return True
    
    def can_drop_col(r,c) :
        for rr in range(r) :
            if board[rr][c] != 0 : return False
        return True
                
    ck = True
    ans = 0
    
    while ck :
        ck = False
        visited = [[False for _ in range(N)] for _ in range(N)]
        for r in range(N) :
            for c in range(N) :
                if board[r][c] != 0 and not visited[r][c]:
                    sr,sc,er,ec = bfs(r,c, visited)
                        
                    if is_rectangle(board[r][c], sr,sc,er,ec) and can_drop(sr,sc,er,ec) :
                        remove(board[r][c], sr,sc,er,ec)
                        ck = True
                        ans += 1
                            
    return ans