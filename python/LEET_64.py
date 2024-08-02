class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = dict()
        R = len(grid)-1
        C = len(grid[0])-1
        INF = 987654321
        def find_dp(r, c) :
            if r == R and c == C : return grid[r][c] 
            if r > R or c > C : return INF
            if (r,c) in dp : return dp[(r,c)]

            dp[(r,c)] = min(find_dp(r+1,c), find_dp(r,c+1)) + grid[r][c]
            return dp[(r,c)]

        return find_dp(0,0)
            