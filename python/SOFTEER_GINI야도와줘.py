import sys
from collections import deque

R,C = map(int, input().split())

board = []

for _ in range(R) :
    board.append(input())

rain = [[-1]*C for _ in range(R)]

q = deque()

sr = -1
sc = -1
er = -1
ec = -1

dr = [-1,0,1,0]
dc = [0,-1,0,1]

for r in range(R) :
    for c in range(C) :
        if board[r][c] == '*' :
            q.append([r,c])
            rain[r][c] = 0
        elif board[r][c] == 'W' :
            sr = r
            sc = c
        elif board[r][c] == 'H' :
            er = r
            ec = c

while q :
    cr,cc = q.popleft()
    for i in range(4) :
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0<=nr<R and 0<=nc<C and rain[nr][nc] == -1 :
            if board[nr][nc] == 'X' or board[nr][nc] == 'H' : continue
            rain[nr][nc] = rain[cr][cc] + 1
            q.append([nr,nc])

visited = [[False]*C for _ in range(R)]
visited[sr][sc] = True
def bfs() :
    q = deque([[sr,sc,0]])
    while q :
        cr,cc,ct = q.popleft()

        if cr == er and cc == ec : 
            print(ct)
            return
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            nt = ct + 1
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and board[nr][nc] != 'X' :
                if rain[nr][nc] != -1 and rain[nr][nc] <= nt : continue
                visited[nr][nc] = True
                q.append([nr,nc,nt])
    print('FAIL')

bfs()
            