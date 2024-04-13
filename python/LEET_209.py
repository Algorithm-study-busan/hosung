INF = 987654321

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        ans = INF
        
        for i, num in enumerate(nums) :
            total += num
            while total - nums[left] >= target :
                total -= nums[left]
                left += 1
            
            if total >= target :
                ans = min(ans, i-left+1)
        
        return 0 if ans == INF else ans
                
            
            