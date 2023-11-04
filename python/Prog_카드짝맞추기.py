from itertools import permutations
from collections import deque

board = []
points = [[] for _ in range(7)]

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def in_range(r,c) :
    return 0<=r<4 and 0<=c<4

def cal_cost(r1, c1, r2, c2) :
    q = deque([[r1, c1]])
    visited = [[-1 for _ in range(4)] for _ in range(4)]
    visited[r1][c1] = 0
    while q :
        cr,cc = q.popleft()
        
        if cr == r2 and cc == c2 : 
            return visited[cr][cc]
        
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            if in_range(nr,nc) and visited[nr][nc] == -1:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append([nr, nc])
                
        for i in range(4) :
            if not in_range(cr+dr[i], cc+dc[i]) : continue
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            while 1 :
                if board[nr][nc] != 0 or not in_range(nr+dr[i], nc+dc[i]): break
                nr += dr[i]
                nc += dc[i]    
            
            if visited[nr][nc] == -1 :
                visited[nr][nc] = visited[cr][cc] + 1
                q.append([nr,nc])
            

def dfs(a, r, c, idx) :
    if idx == len(a) : return 0
    r1 = points[a[idx]][0][0]
    c1 = points[a[idx]][0][1]
    r2 = points[a[idx]][1][0]
    c2 = points[a[idx]][1][1]
    
    nxt1 = 0
    nxt1 += cal_cost(r,c, r1, c1)+1
    nxt1 += cal_cost(r1,c1, r2,c2)+1
    tmp = board[r1][c1]
    board[r1][c1] = 0
    board[r2][c2] = 0
    nxt1 += dfs(a, r2, c2, idx+1)
    
    nxt2 = 0
    board[r1][c1] = tmp
    board[r2][c2] = tmp
    nxt2 += cal_cost(r,c, r2,c2)+1
    nxt2 += cal_cost(r2,c2, r1, c1)+1
    board[r1][c1] = 0
    board[r2][c2] = 0
    nxt2 += dfs(a, r1, c1, idx+1)
    
    board[r1][c1] = tmp
    board[r2][c2] = tmp
    
    return min(nxt1, nxt2)

def solution(board_, sr, sc):
    global board, points
    board = board_
    
    num_set = set()
    for r in range(4) :
        for c in range(4) :
            if board[r][c] != 0 :
                points[board[r][c]].append([r,c])
                num_set.add(board[r][c])
                
    arr = sorted(list(num_set))
    ans = 987654321
    for a in permutations(arr) :
        ans = min(ans, dfs(a, sr, sc, 0))
    return ans
    
    
print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1,0))

print(cal_cost(1,0, 1,0))
print(cal_cost(1,0, 2,3))
board[1][0] = 0
board[2][3] = 0

print(cal_cost(2,3,0,3))
print(cal_cost(0,3,3,0))
board[0][3] = 0
board[3][0] = 0

print(cal_cost(3,0,3,2))
print(cal_cost(3,2,0,0))
