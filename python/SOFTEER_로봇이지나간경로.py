import sys

R,C = map(int, input().split())

board = []

for _ in range(R) :
    board.append(input())

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def count(r,c) :
    ret = 0 
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<R and 0<=nc<C and board[nr][nc] == '#' :
            ret += 1
    return ret
            
sr = -1
sc = -1
for r in range(R) :
    for c in range(C) :
        if board[r][c] == '#' and count(r,c) == 1 : 
            sr = r
            sc = c

visited = [[False] * C for _ in range(R)]

d = -1

for i in range(4) :
    nr = sr + dr[i]
    nc = sc + dc[i]
    if 0<=nr<R and 0<=nc<C and board[nr][nc] == '#' :
        d = i

print(sr+1, sc+1)

arrow = ['^', '>', 'v', '<']

sd = arrow[d]
visited[sr][sc] = True

ans = ""

while True :
    for _ in range(2) :
        sr += dr[d]
        sc += dc[d]
        visited[sr][sc] = True
    ans += 'A'

    nd = -1
    for i in range(4) :
        nr = sr + dr[i]
        nc = sc + dc[i]
        if 0<=nr<R and 0<=nc<C and board[nr][nc] == '#' and not visited[nr][nc] :
            nd = i
    if nd == -1 : break
    if d == 3 and nd == 0 : ans += 'R'
    elif d == 0 and nd == 3 : ans += 'L'
    elif d < nd : ans += 'R'
    elif d > nd : ans += 'L'
    d = nd

print(sd)
print(ans)