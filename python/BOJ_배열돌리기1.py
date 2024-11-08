from collections import deque

R,C, k = map(int, input().split())

board = []
for _ in range(R) :
    board.append( list(map(int, input().split())) )

arrs = []

def makeQ(i) :
    q  = deque()
    
    for r in range(i, R-1-i) :
        q.append(board[r][i])
    for c in range(i, C-1-i) :
        q.append(board[R-1-i][c])
    for r in range(R-1-i, i, -1) :
        q.append(board[r][C-1-i])
    for c in range(C-1-i, i, -1) :
        q.append(board[i][c])
        
    return q
        
def makeBoard(q, i) :
    for r in range(i, R-1-i) :
        board[r][i] = q.popleft()
    for c in range(i, C-1-i) :
        board[R-1-i][c] = q.popleft()
    for r in range(R-1-i, i, -1) :
        board[r][C-1-i] = q.popleft()
    for c in range(C-1-i, i, -1) :
        board[i][c] = q.popleft()
            

qs = []
for i in range(min(R,C)//2) :
    qs.append(makeQ(i))
    
for q in qs :
    q.rotate(k%len(q))
    
for i in range(min(R,C)//2) :
    makeBoard(qs[i], i)
    
for row in board :
    print(*row)
