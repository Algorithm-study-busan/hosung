def win(board_num, isO) :
    k = 3
    if not isO : k *= -1
    
    for i in range(3) :
        if (sum(board_num[i]) == k or
            sum(board_num[0][i] + board_num[1][i] + board_num[2][i]) == k) : return True
    
    tmp = 0
    for i in range(3) :
        tmp += board_num[i][i]
    if tmp == k : return True
    
    tmp = 0 
    for i in range(3) :
        tmp += board_num[i][2-i]
    if tmp == k : return True
    
    return False
    
    
    

def solution(board):
    board_num = [[0 for _ in range(3)] for _ in range(3)]
    
    mapping = {'O' : 1, '.' : 0, 'X' : -1}
    
    cnt_O = 0
    cnt_X = 0
    
    for i in range(3) :
        for j in range(3) :
            board_num = mapping(board[i][j])
            if board_num[i][j] == 1 : cnt_O += 1
            elif board_num[i][j] == -1 : cnt_X += 1
            
    O_win = win(board_num, True)
    X_win = win(board_num, False)
    
    if O_win and X_win : return -1
    
    if cnt_O == cnt_X :
        if O_win : return -1
        return 1
    elif cnt_O+1 == cnt_X :
        if X_win : return -1
        return 1
    return -1