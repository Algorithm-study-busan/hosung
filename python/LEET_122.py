class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_stock = prices[0]
        max_stock = prices[0]
        for p in prices[1:] :
            if p > max_stock :
                max_stock = p
            else :
                ans += max_stock - min_stock 
                min_stock = p
                max_stock = p
        ans += max_stock - min_stock
        return ans

        