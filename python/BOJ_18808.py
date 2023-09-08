from sys import stdin
input = stdin.readline

R,C,K = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
stickers = []

def is_stickable(board, sticker, r, c) :
    if r + len(sticker) > R or c + len(sticker[0]) > C : return False
    
    for i in range(len(sticker)) :
        for j in range(len(sticker[0])) :
            if sticker[i][j] == 1 and board[r+i][c+j] == 1 : return False
    return True

def stick(board, sticker, r,c) :
    for i in range(len(sticker)) :
        for j in range(len(sticker[0])) :
            if sticker[i][j] == 1 :
                board[r+i][c+j] = 1

def one_cycle(board, sticker) :
    for r in range(R) :
        for c in range(C) :
            if is_stickable(board, sticker, r, c) :
                stick(board, sticker, r, c)
                return True
    return False
                
def rotate(sticker) :
    SR = len(sticker)
    SC = len(sticker[0])
    rotated = [[0 for _ in range(SR)] for _ in range(SC)]

    for r in range(SC) :
        for c in range(SR) :
            rotated[r][c] = sticker[SR-1-c][r]
    return rotated

for _ in range(K) :
    r,c = map(int, input().split())
    sticker = []
    for _ in range(r) :
        col = list(map(int, input().split()))
        sticker.append(col)
    stickers.append(sticker)

for sticker in stickers :
    for _ in range(4) :
        if one_cycle(board, sticker) : break
        sticker = rotate(sticker)
        
ans = 0
for r in range(R) :
    for c in range(C) :
        ans += board[r][c]

print(ans)
        
    
                