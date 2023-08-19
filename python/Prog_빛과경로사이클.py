    def get_na(a, d) :
        if d == 'L' : a -= 1
        elif d == 'R' : a += 1
        return (a + 4)%4

    dr = [
        {'S' : 1, 'L' : 0, 'R' : 0},
        {'S' : 0, 'L' : 1, 'R' : -1},
        {'S' : -1, 'L' : 0, 'R' : 0},
        {'S' : 0, 'L' : -1, 'R' : 1}
    ]
    dc = [
        {'S' : 0, 'L' : 1, 'R' : -1},
        {'S' : -1, 'L' : 0, 'R' : 0},
        {'S' : 0, 'L' : -1, 'R' : 1},
        {'S' : 1, 'L' : 0, 'R' : 0}
    ]


    def solution(grid):
        R = len(grid)
        C = len(grid[0])
        
        visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
        
        ans = []
        for r in range(R) :
            for c in range(C) :
                for a in range(4) :
                    tmp = 0
                    while not visited[r][c][a] :
                        tmp += 1
                        visited[r][c][a] = True
                        nr = r + dr[a][grid[r][c]]
                        nc = c + dc[a][grid[r][c]]
                        na = get_na(a, grid[r][c])
                        
                        r = (nr + R)%R
                        c = (nc + C)%C
                        a = na
                    if tmp != 0 : ans.append(tmp)
                    
        ans.sort()
        return ans