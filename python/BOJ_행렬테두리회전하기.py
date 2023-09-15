def rotate(board, r1,c1, r2,c2) :
    last = board[r1][c1]
    ret = last
    
    for c in range(c1+1, c2+1) :
        tmp = board[r1][c]
        board[r1][c] = last
        last = tmp
        ret = min(ret, last)
        
    for r in range(r1+1, r2+1) :
        tmp = board[r][c2]
        board[r][c2] = last
        last = tmp
        ret = min(ret, tmp)
        
    for c in range(c2-1, c1-1, -1) :
        tmp = board[r2][c]
        board[r2][c] = last
        last = tmp
        ret = min(ret, tmp)
        
    for r in range(r2-1, r1-1, -1) :
        tmp = board[r][c1]
        board[r][c1] = last 
        last = tmp
        ret = min(ret, tmp)
    
    return ret
    
    
    

def solution(rows, columns, queries):
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for r in range(rows) :
        for c in range(columns) :
            board[r][c] = r*columns + c + 1
    ans = []
    for r1,c1, r2,c2 in queries :
        ans.append(rotate(board, r1-1,c1-1, r2-1,c2-1))
    return ans