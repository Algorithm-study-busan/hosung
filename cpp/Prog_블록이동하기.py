from collections import deque

MAX = 100
INF = 987654321
N = 0
board = []

dr = [0,1,0,-1]
dc = [1,0,-1,0]
visited = [[[INF for _ in range(4)] for _ in range(MAX)] for _ in range(MAX)]

def inRange(r, c, k) :
    return 0<=r<N and 0<=c<N and 0<=r+dr[k]<N and 0<=c+dc[k]<N

def isWall(r, c, k) :
    return board[r][c] == 1 or board[r + dr[k]][c + dc[k]] == 1

def bfs() :
    visited[0][0][0] = 0
    q = deque([[0,0,0]])

    while q :
        cr, cc, ck = q.popleft()
        pr = cr + dr[ck]
        pc = cc + dc[ck]

        print(cr, cc, ck, visited[cr][cc][ck])

        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if inRange(nr, nc, ck) and not isWall(nr,nc,ck) and visited[nr][nc][ck] > visited[cr][cc][ck] + 1 :
                visited[nr][nc][ck] = visited[cr][cc][ck] + 1
                q.append([nr,nc,ck])
        
        if cr == pr :
            if cr > 0 and board[cr-1][cc] == 0 and board[pr-1][pc] == 0 :
                if visited[cr][cc][3] > visited[cr][cc][ck] + 1 :
                    visited[cr][cc][3] = visited[cr][cc][ck] + 1
                    q.append([cr,cc,3])
                if visited[pr][pc][3] > visited[cr][cc][ck] + 1 :
                    visited[pr][pc][3] = visited[cc][cc][ck] + 1
                    q.append([pr,pc,3])

            if cr < N-1 and board[cr+1][cc] == 0 and board[pr+1][pc] == 0 :
                if visited[cr][cc][1] > visited[cr][cc][ck] + 1 :
                    visited[cr][cc][1] = visited[cr][cc][ck] + 1
                    q.append([cr,cc,1])
                if visited[pr][pc][1] > visited[cr][cc][ck] + 1 :
                    visited[pr][pc][1] = visited[cr][cc][ck] + 1
                    q.append([pr,pc,1])
        
        if cc == pc :
            if cc > 0 and board[cr][cc-1] == 0 and board[pr][pc-1] == 0 :
                if visited[cr][cc][2] > visited[cr][cc][ck] + 1 :
                    visited[cr][cc][2] = visited[cr][cc][ck] + 1
                    q.append([cr,cc,2])
                if visited[pr][pc][2] > visited[cr][cc][ck] + 1 :
                    visited[pr][pc][2] = visited[cr][cc][ck] + 1
                    q.append([pr,pc,2])
            if cc < N-1 and board[cr][cc+1] == 0 and board[pr][pc+1] == 0 :
                if visited[cr][cc][0] > visited[cr][cc][ck] + 1 :
                    visited[cr][cc][0] = visited[cr][cc][ck] + 1
                    q.append([cr,cc,0])
                if visited[pr][pc][0] > visited[cr][cc][ck] + 1 :
                    visited[pr][pc][0] = visited[cr][cc][ck] + 1
                    q.append([pr,pc,0])

    return

        

def solution(board_):
    global N, board
    board = board_
    N = len(board)
    bfs()
    return min(visited[N-1][N-2][0], visited[N-1][N-1][2], 
               visited[N-2][N-1][1], visited[N-1][N-1][3])

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))