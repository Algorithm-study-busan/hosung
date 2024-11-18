R,C,K = map(int, input().split())
board = []

for _ in range(R) :
    board.append(input())
    
black_row_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]
black_col_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]

white_row_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]
white_col_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]

for r in range(R) : 
    for c in range(C) :
        k = (board[r][c] == 'B' and (r+c) % 2 == 1) or (board[r][c] == 'W' and (r+c) % 2 == 0)
        black_row_sum[r+1][c+1] = black_row_sum[r+1][c] + k
        white_row_sum[r+1][c+1] = white_row_sum[r+1][c] + (not k)
        
for c in range(C) :
    for r in range(R) :
        k = (board[r][c] == 'B' and (r+c) % 2 == 1) or (board[r][c] == 'W' and (r+c) % 2 == 0)
        black_col_sum[r+1][c+1] = black_col_sum[r][c+1] + k
        white_col_sum[r+1][c+1] = white_col_sum[r][c+1] + (not k)
        
black_square_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]
white_square_sum = [[0 for _ in range(C+1)] for _ in range(R+1)]

for r in range(R) :
    for c in range(C) :
        k = (board[r][c] == 'B' and (r+c) % 2 == 1) or (board[r][c] == 'W' and (r+c) % 2 == 0)
        black_square_sum[r+1][c+1] = black_square_sum[r][c] + black_row_sum[r+1][c+1] + black_col_sum[r+1][c+1] - k
        white_square_sum[r+1][c+1] = white_square_sum[r][c] + white_row_sum[r+1][c+1] + white_col_sum[r+1][c+1] - (not k)
        
        
ans = 987654321
for r in range(K-1,R) :
    for c in range(K-1, C) :
        tmp_black = black_square_sum[r+1][c+1] - black_square_sum[r+1-K][c+1] - black_square_sum[r+1][c+1-K] + black_square_sum[r+1-K][c+1-K]
        tmp_white = white_square_sum[r+1][c+1] - white_square_sum[r+1-K][c+1] - white_square_sum[r+1][c+1-K] + white_square_sum[r+1-K][c+1-K]
        
        ans = min(ans, tmp_black, tmp_white)
        
print(ans)