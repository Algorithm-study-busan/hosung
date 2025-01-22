class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        start = 0
        tmp = 0
        ans = 0
        for i,n in enumerate(nums) :
            if n == 0 :
                if k > 0 :
                    tmp = i
                    k -= 1
                else :
                    start = tmp+1
                    tmp = i
            ans = max(ans, i-start) 
        return ans
                
            
         