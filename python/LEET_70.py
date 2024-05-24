class Solution:
    def __init__(self) :
        self.dp = [-1 for _ in range(46)]

    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        if n == 2 : return 2
        if self.dp[n] != -1 : return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        