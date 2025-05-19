from collections import deque

R,C = map(int, input().split())

sr, sc = map(int, input().split())
er, ec = map(int, input().split())

board = []

for _ in range(R) :
    board.append(list(map(int, input().split())))

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def bfs() :
    visited = [[[-1, -1] for _ in range(C)] for _ in range(R)]
    q = deque([[sr-1, sc-1, 0]])
    visited[sr-1][sc-1][0] = 0
    
    while q :
        cr, cc, ck = q.popleft()
        if cr == er-1 and cc == ec -1 :
            print(visited[cr][cc][ck])
            return
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            nk = ck
            if nr < 0 or nr >= R or nc < 0 or nc >= C : continue
            if board[nr][nc] == 1 :
                if nk == 1 : continue
                else : nk += 1
            if visited[nr][nc][nk] >= 0 : continue 
            visited[nr][nc][nk] = visited[cr][cc][ck] + 1
            q.append([nr,nc,nk])
            
    print(-1)
                    
                
bfs()