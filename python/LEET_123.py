class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0 for _ in range(len(prices))]
        right = [0 for _ in range(len(prices))]

        tmp = prices[0]
        for i in range(1, len(prices)) :
            tmp = min(tmp, prices[i])
            left[i] = max(left[i-1], prices[i] - tmp)

        tmp = prices[-1]
        for i in range(len(prices)-2, -1, -1) :
            tmp = max(tmp, prices[i])
            right[i] = max(right[i+1], tmp - prices[i])

        ans = max(left[-1], right[0])
        for i in range(len(prices)-1) :
            ans = max(ans, left[i] + right[i+1])
        return ans

        