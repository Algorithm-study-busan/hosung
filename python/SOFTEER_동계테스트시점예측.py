import sys
from collections import deque

R,C = map(int, input().split())

board = []

for _ in range(R) :
    board.append(list(map(int, input().split())))

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def air(r, c) :
    q = deque([[r,c]])
    board[r][c] = 2
    while q :
        cr,cc = q.popleft()

        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<R and 0<=nc<C and board[nr][nc] == 0 :
                board[nr][nc] = 2
                q.append([nr,nc])


for r in range(R) :
    if board[r][0] == 0 : air(r,0)
    if board[r][C-1] == 0 : air(r, C-1)

for c in range(C) :
    if board[0][c] == 0 : air(0, c)
    if board[R-1][c] == 0 : air(R-1, c)

def is_melt(r,c) :
    cnt = 0
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<R and 0<=nc< C and board[nr][nc] == 2 : cnt += 1

    return cnt >= 2

ans = 0

while True :
    melted = []
    for r in range(R) :
        for c in range(C) :
            if board[r][c] == 1 and is_melt(r,c) :
                melted.append([r,c])

    if not melted : break

    ans += 1
    for r,c in melted :
        air(r,c)

print(ans)
                
            
        
        