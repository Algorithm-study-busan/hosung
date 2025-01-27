import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))


dp_start = [[0 for _ in range(N)] for _ in range(N)]
dp_end = [[0 for _ in range(N)] for _ in range(N)]

def get_start(r,c) :
    if r < 0 or c < 0  : return 0
    return dp_start[r][c]

def get_end(r,c) :
    if r >= N or c >= N : return 0
    return dp_end[r][c]

for r in range(N) :
    for c in range(N) :
        dp_start[r][c] = board[r][c] + max(get_start(r-1,c), get_start(r,c-1))

for r in range(N-1, -1, -1) :
    for c in range(N-1, -1, -1) :
        dp_end[r][c] = board[r][c] + max(get_end(r+1,c), get_end(r,c+1))

ans = 0
for r in range(N) :
    for c in range(N) :
        ans = max(ans, dp_start[r][c] + dp_end[r][c])
print(ans)
    