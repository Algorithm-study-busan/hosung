def solution(line):
    meet = []
    for i in range(len(line)) :
        for j in range(i+1, len(line)) :
            u = (line[i][0]*line[j][2]) - (line[j][0]*line[i][2])
            d = (line[j][0]*line[i][1]) - (line[i][0]*line[j][1])
            if d == 0 : continue
            y = u / d
            if y != int(y) : continue
            
            u = (line[i][1]*line[j][2]) - (line[i][2]*line[j][1])
            d = (line[i][0]*line[j][1]) - (line[i][1]*line[j][0])
            if d == 0 : continue
            x = u / d
            if x != int(x) : continue
            
            meet.append([int(x), int(y)])
    
    meet.sort(key=lambda x : x[0])
    X = meet[-1][0] - meet[0][0] + 1
    sx = meet[0][0]
    meet.sort(key=lambda x : x[1])
    Y = meet[-1][1] - meet[0][1] + 1
    sy = meet[-1][1]
    
    board = []
    for _ in range(Y) :
        board.append(['.']*X)
        
    for x,y in meet :
        board[sy-y][x - sx] = '*'
    ans = []
    for b in board :
        ans.append("".join(b))
    return ans
                
            
            