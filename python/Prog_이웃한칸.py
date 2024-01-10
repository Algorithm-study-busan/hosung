dr = [-1,0,1,0]
dc = [0,-1,0,1]

def solution(board, h, w):
    ans = 0
    R = len(board)
    C = len(board[0])
    for i in range(4) :
        nr = h + dr[i]
        nc = w + dc[i]
        
        if 0<=nr<R and 0<=nc<C and board[nr][nc] == board[h][w]: ans += 1
    return ans
            