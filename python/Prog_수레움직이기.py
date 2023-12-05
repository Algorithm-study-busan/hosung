R = 0
C = 0
INF = 987654321
ans = INF

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def dfs(board, red_visited, blue_visited, rr,rc,br,bc, cnt) :
    print(rr, rc, br, bc, cnt)
    global ans
    if board[rr][rc] == 3 and board[br][bc] == 4 :
        ans = min(ans, cnt)
        return

    elif board[br][bc] == 4 :
        for i in range(4) :
            nrr = rr + dr[i]
            nrc = rc + dc[i]
            
            if (0<=nrr<R and 0<=nrc<C) and (board[nrr][nrc] != 5) and (not red_visited[nrr][nrc]) and (nrr != br or nrc != bc):
                red_visited[nrr][nrc] = True
                dfs(board, red_visited, blue_visited, nrr, nrc, br, bc, cnt+1)
                red_visited[nrr][nrc] = False
    
    elif board[rr][rc] == 3 : 
        for i in range(4) :
            nbr = br + dr[i]
            nbc = bc + dc[i]
            
            if (0<=nbr<R and 0<=nbc<C) and (board[nbr][nbc] != 5) and (not blue_visited[nbr][nbc]) and (nbr != rr or nbc != rc) :
                blue_visited[nbr][nbc] = True
                dfs(board, red_visited, blue_visited, rr, rc, nbr, nbc, cnt+1)
                blue_visited[nbr][nbc] = False
    
    else : 
        for i in range(4) :
            nrr = rr + dr[i]
            nrc = rc + dc[i]
            
            if (0<=nrr<R and 0<=nrc<C) and (board[nrr][nrc] != 5) and (not red_visited[nrr][nrc]):
                
                if nrr == br and nrc == bc : 
                    for j in range(4) :
                        nbr = br + dr[j]
                        nbc = bc + dc[j]
                        if (0<=nbr<R and 0<=nbc<C) and (board[nbr][nbc] != 5) and (not blue_visited[nbr][nbc]) and (nbr != rr or nbc != rc) :
                            red_visited[nrr][nrc] = True
                            blue_visited[nbr][nbc] = True
                            dfs(board, red_visited, blue_visited, nrr, nrc, nbr, nbc, cnt+1)
                            red_visited[nrr][nrc] = False
                            blue_visited[nbr][nbc] = False
                else :      
                    for j in range(4) :
                        nbr = br + dr[j]
                        nbc = bc + dc[j]
                        
                        if (0<=nbr<R and 0<=nbc<C) and (board[nbr][nbc] != 5) and (not blue_visited[nbr][nbc]) and (nbr != nrr or nbc != nrc) :
                            red_visited[nrr][nrc] = True
                            blue_visited[nbr][nbc] = True
                            dfs(board, red_visited, blue_visited, nrr, nrc, nbr, nbc, cnt+1)
                            red_visited[nrr][nrc] = False
                            blue_visited[nbr][nbc] = False
                        
       
                
            
                
            
        

def solution(maze):
    global R,C
    R = len(maze)
    C = len(maze[0])
    
    rr, rc = 0,0
    br, bc = 0,0
    
    for r in range(R) :
        for c in range(C) :
            if maze[r][c] == 1 :
                rr = r
                rc = c
            elif maze[r][c] == 2 :
                br = r
                bc = c
    
    red_visited = [[False for _ in range(C)] for _ in range(R)]
    blue_visited = [[False for _ in range(C)] for _ in range(R)]
    red_visited[rr][rc] = True
    blue_visited[br][bc] = True
    dfs(maze, red_visited, blue_visited, rr, rc, br, bc, 0)
    if ans == INF : return 0
    return ans
    
    