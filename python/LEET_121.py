class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_stock = prices[0]
        for i in range(1, len(prices)) :
            ans = max(ans, prices[i] - min_stock)
            min_stock = min(min_stock, prices[i])
        return ans
        