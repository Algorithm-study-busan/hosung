import sys
from itertools import product

N,M = map(int, input().split())

board = []

for _ in range(N) :
    board.append(list(map(int, input().split())))

starts = []

for _ in range(M) :
    r,c = map(int, input().split())
    starts.append([r-1,c-1])

dr = [-1,0,1,0]
dc = [0,-1,0,1]

ans = 0

def cal(moves) :
    tmp = 0
    tmp_starts = []
    visited = set()
    
    for r,c in starts :
        tmp_starts.append([r,c])
        tmp += board[r][c]
        visited.add(tuple([r,c]))
    
    for i in range(3) :
        sync_visited = set()
        for j in range(M) :
            nr = tmp_starts[j][0] + dr[moves[j][i]]
            nc = tmp_starts[j][1] + dc[moves[j][i]]
            
            if 0<=nr<N and 0<=nc<N and tuple([nr,nc]) not in sync_visited : 
                sync_visited.add(tuple([nr,nc]))
                
                if tuple([nr,nc]) not in visited :
                    visited.add(tuple([nr,nc]))
                    tmp += board[nr][nc]
                    
                tmp_starts[j][0] = nr
                tmp_starts[j][1] = nc
            else :
                return -987654321
    return tmp
        
            

def dfs(moves, i) :
    global ans
    if i == M :
        ans = max(ans, cal(moves))
        return
    for m in product([0,1,2,3], repeat = 3) :
        moves.append(m)
        dfs(moves, i+1)
        moves.pop()

dfs([], 0)
print(ans)
