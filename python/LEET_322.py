class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 987654321
        dp = [-1 for _ in range(10_001)]

        dp[0] = 0
        def find_dp(x) :
            if dp[x] != -1 : return dp[x]

            dp[x] = INF
            for coin in coins :
                if x >= coin :
                    dp[x] = min(dp[x], 1 + find_dp(x-coin))
            return dp[x]

        find_dp(amount)
        return -1 if dp[amount] == INF else dp[amount]