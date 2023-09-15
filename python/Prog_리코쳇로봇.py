from collections import deque


dr = [-1,0,1,0]
dc = [0,1,0,-1]
R = -1
C = -1
board = [[]]
visited = [[]]

def in_range(r, c) :
    return 0<=r<R and 0<=c<C

def next_position(r, c, i) :
    while in_range(r + dr[i], c + dc[i]) and board[r+dr[i]][c+dc[i]] != 'D' :
        r += dr[i]
        c += dc[i]
    return (r,c)

def bfs(r, c) :
    q = deque([(r,c)])
    visited[r][c] = 0
    while q :
        cr, cc = q.popleft()
        
        if board[cr][cc] == "G" :
            return visited[cr][cc]
        
        for i in range(4) :
            nr,nc = next_position(cr,cc,i)
            if visited[nr][nc] >= 0 : continue
            
            visited[nr][nc] = visited[cr][cc] + 1
            q.append((nr,nc))
            
    return -1
    
    

def solution(b):
    global R,C, board, visited
    board = b
    R = len(board)
    C = len(board[0])
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    
    sr = 0
    sc = 0
    for r in range(R) :
        for c in range(C) :
            if board[r][c] == "R" :
                sr = r
                sc = c
    
    
    ans = bfs(sr,sc)
    for r in range(R) :
        print(*visited[r])
    return ans