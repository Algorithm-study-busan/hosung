class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = dict()

        def find_dp(r,c) :
            if (r,c) in dp : return dp[(r,c)]
            if r == len(triangle)-1 : return triangle[r][c]
            dp[(r,c)] = min(find_dp(r+1, c), find_dp(r+1, c+1)) + triangle[r][c]
            return dp[(r,c)]

        return find_dp(0,0)
