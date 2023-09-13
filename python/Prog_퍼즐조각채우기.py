from collections import deque

N = 0
dr = [-1,0,1,0]
dc = [0,-1,0,1]

def is_equal(p1, p2) :
    p1.sort()
    p2.sort()
    if len(p1) != len(p2) : return False
    mr = p1[0][0] - p2[0][0]
    mc = p1[0][1] - p2[0][1]
    
    for i in range(len(p1)) :
        if p1[i][0] != p2[i][0] + mr or p1[i][1] != p2[i][1] + mc : return False
    return True

def in_range(r, c) :
    return 0<=r<N and 0<=c<N

def find_puzzle(board, r,c, visited, k) :
    q = deque([[r,c]])
    visited[r][c] = True
    ret = []
    while q :
        cr,cc = q.popleft()
        ret.append([cr,cc])
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if not in_range(nr,nc) or visited[nr][nc] or board[nr][nc] == k : continue
            visited[nr][nc] = True
            q.append([nr,nc])
    return ret

def find_puzzle_only(board, r,c, k) :
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([[r,c]])
    visited[r][c] = True
    ret = []
    while q :
        cr,cc = q.popleft()
        ret.append([cr,cc])
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if not in_range(nr,nc) or visited[nr][nc] or board[nr][nc] == k : continue
            visited[nr][nc] = True
            q.append([nr,nc])
    return ret

def solution(game_board, table):
    global N
    N = len(game_board)
    tables = [table]
    
    for _ in range(3) :
        new_table = []
        for c in range(N) :
            arr = []
            for r in range(N-1,-1,-1) :
                arr.append(tables[-1][r][c])
            new_table.append(arr)
        tables.append(new_table)
        
    b_arr = []
    t_arr = []
    b_visited = [[False for _ in range(N)] for _ in range(N)]
    
    
    for r in range(N) :
        for c in range(N) :
            if game_board[r][c] == 0 and not b_visited[r][c] :
                b_arr.append(find_puzzle(game_board, r,c, b_visited, 1))
                
    
    t_visited = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N) :
        for c in range(N) :
            if tables[0][r][c] == 1 and not t_visited[r][c] :
                puzzle = []
                puzzle.append(find_puzzle(tables[0], r, c, t_visited, 0))
                puzzle.append(find_puzzle_only(tables[1], c,N-r-1, 0))
                puzzle.append(find_puzzle_only(tables[2], N-r-1,N-c-1, 0))
                puzzle.append(find_puzzle_only(tables[3], N-1-c,r, 0))
                t_arr.append(puzzle)
            
    ans = 0
    used = [False for _ in range(len(t_arr))]
    flag = True
    for b in b_arr :
        flag = False
        for i,ts in enumerate(t_arr) :
            if flag : break
            if used[i] : continue
            for t in ts :
                if is_equal(b, t) : 
                    ans += len(t)
                    used[i] = True
                    flag = True
                    break
    return ans