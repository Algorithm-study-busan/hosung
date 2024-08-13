from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dr = [0,-1,0,1]
        dc = [-1,0,1,0]

        visited = [[False for _ in range(C)] for _ in range(R)]

        def bfs(r, c) :
            q = deque([[r,c]])
            visited[r][c] = True

            cnt = 0
            while q :
                cr,cc = q.popleft()
                cnt += 1
                for i in range(4) :
                    nr = cr + dr[i]
                    nc = cc + dc[i]

                    if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1 and not visited[nr][nc] :
                        visited[nr][nc] = True
                        q.append([nr,nc])

            return cnt


        ans = 0
        for r in range(R) :
            for c in range(C) :
                if grid[r][c] == 1 and not visited[r][c] :
                    ans = max(ans, bfs(r,c))
        return ans
        
        
        