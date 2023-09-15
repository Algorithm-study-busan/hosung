from collections import deque

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def in_range(r, c) :
    return 0<=r<5 and 0<=c<5

def bfs(board, r, c) :
    dist = [[[-1 for _ in range(2)] for _ in range(5)] for _ in range(5)]
    q = deque([[r,c, 0]])
    dist[r][c][0] = 0
    while q :
        cr,cc,cp = q.popleft()
        
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            np = cp
            if not in_range(nr,nc) : continue
            if board[nr][nc] == 'X' : np = 1
            
            if dist[nr][nc][np] != -1 : continue
            dist[nr][nc][np] = dist[cr][cc][cp] + 1
            
            if board[nr][nc] == 'P' and dist[nr][nc][np] <= 2 and np == 0 : return False
            q.append([nr,nc,np])
    return True

def is_distancing(board) :
    for r in range(5) :
        for c in range(5) :
            if board[r][c] == 'P' and not bfs(board, r,c):
                return 0
    return 1
    

def solution(places):
    answer = []
    for place in places :
        answer.append(is_distancing(place))
    return answer