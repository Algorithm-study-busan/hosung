INF = 987654321

board = [[]]
target = [[]]
R = 0
C = 0

ans = INF

def changeR(r) :
    for c in range(C) : 
        board[r][c] = (board[r][c] + 1) % 2
        
def changeC(c) :
    for r in range(R) :
        board[r][c] = (board[r][c] + 1) % 2
        
        
def dfs(idx, cnt) :
    global ans
    if idx == R*C :
        if board == target :
            ans = min(ans, cnt)
        return
    
    r = idx // C
    c = idx % C
    if board[r][c] == target[r][c] :
        dfs(idx+1, cnt)
    else :
        changeR(r)
        dfs(idx+1, cnt+1)
        changeR(r)
        
        changeC(c)
        dfs(idx+1, cnt+1)
        changeC(c)
    

def solution(beginning, t):
    global board, target, R,C
    board = beginning
    target = t
    R = len(board)
    C = len(board[0])
    
    dfs(0,0)
    
    return -1 if ans == INF else ans
    