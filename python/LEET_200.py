from collections import deque

dr = [-1,0,1,0]
dc = [0,-1,0,1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        ans = 0

        for r in range(R) :
            for c in range(C) : 
                if grid[r][c] == '1' and not visited[r][c] :
                    ans += 1
                    q = deque([[r,c]])
                    while q :
                        cr,cc = q.pop()
                        for i in range(4) :
                            nr = cr + dr[i]
                            nc = cc + dc[i]
                            if 0<=nr<R and 0<=nc<C and grid[nr][nc] == '1' and not visited[nr][nc] :
                                visited[nr][nc] = True
                                q.append([nr,nc])

        return ans


        