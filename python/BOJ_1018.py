R,C = map(int, input().split())
board = []
for _ in range(R) :
    board.append(input())

def cal(r,c) :
    x = ['W', 'B'] 
    
    ret1 = 0
    ret2 = 0
    
    for nr in range(r, r+8) :
        for nc in range(c, c+8) :
            if board[nr][nc] != x[(nr+nc)%2] : ret1 += 1
            else : ret2 += 1
            
    return min(ret1, ret2)

ans = 987654321

for r in range(R-7) :
    for c in range(C-7) :
        ans = min(ans, cal(r,c))
            
print(ans)
    
