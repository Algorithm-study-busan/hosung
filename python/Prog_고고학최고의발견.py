import copy

board = []
R = 0

dr = [-1,0,1,0]
dc = [0,-1,0,1]

ans = 987654321

def in_range(r, c) :
    return 0<=r<R and 0<=c<R

def move(r, c, board_, k) :
    board_[r][c] = (board_[r][c]+k)%4
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if not in_range(nr,nc) : continue
        board_[nr][nc] = (board_[nr][nc]+k)%4
        
def dfs(c, cnt) :
    if c == R : 
        cal_cnt(copy.deepcopy(board), cnt)
        return
    dfs(c+1, cnt)
    for k in range(1,4) :
        move(0, c, board, k)
        dfs(c+1, cnt+k)
        move(0, c, board, 4-k)
        
def cal_cnt(copy_board, cnt) :
    global ans
    ret = cnt
    for r in range(R-1) :
        for c in range(R) :
            if copy_board[r][c] != 0 :
                ret += 4-copy_board[r][c]
                move(r+1, c, copy_board, 4-copy_board[r][c])
                    
    for c in range(R) :
        if copy_board[R-1][c] != 0 : return 
    ans = min(ans, ret)

def solution(clockHands):
    global board, R
    board = clockHands
    R = len(board)
    
    dfs(0, 0)
    return ans