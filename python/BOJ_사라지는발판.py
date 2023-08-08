dr = [-1,0,1,0]
dc = [0,-1,0,1]

def win(board, ar, ac, br, bc, order) :
    if order :
        if board[ar][ac] == 0 : return [False, 0]
        board[ar][ac] = 0
        
        ret = False
        win_arr = []
        lose_arr = []

        for i in range(4) :
            nr = ar + dr[i]
            nc = ac + dc[i]
            if not (0<=nr<len(board) and 0<=nc<len(board[0])) or board[nr][nc] == 0  : continue
            
            result = win(board, nr, nc, br, bc, (order+1)%2)
            ret = ret or result[0]
            
            if result[0] : win_arr.append(result[1]+1)
            else : lose_arr.append(result[1]+1)
            
        board[ar][ac] = 1
        
        if ret : return [ret, min(win_arr)]
        else : 
            if len(lose_arr) == 0 : return [ret, 0]
            else : return [ret, max(lose_arr)]
    
    else :
        if board[br][bc] == 0 : return [True, 0]
        board[br][bc] = 0
        
        ret = True
        win_arr = []
        lose_arr = []
        
        for i in range(4) :
            nr = br + dr[i]
            nc = bc + dc[i]
            if not (0<=nr<len(board) and 0<=nc<len(board[0])) or board[nr][nc] == 0 : continue
            
            result = win(board, ar, ac, nr, nc, (order+1)%2)
            ret = ret and result[0]
            
            if not result[0] : win_arr.append(result[1]+1)
            else : lose_arr.append(result[1]+1)
            
        board[br][bc] = 1
        
        if not ret : return [ret, min(win_arr)]
        else : 
            if len(lose_arr) == 0 : return [ret, 0]
            else : return [ret, max(lose_arr)]

def solution(board, aloc, bloc):
    return win(board, aloc[0], aloc[1], bloc[0], bloc[1], 1)[1]


print(solution([[1,1,1], [1,1,1], [1,1,1]], [1,0], [0,0]))