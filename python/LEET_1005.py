class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 0
        zero = False
        min_abs = 101
        for n in nums :
            if k > 0 and n < 0 : 
                ans += -n
                k -= 1
            else : 
                ans += n
            if n == 0 : zero = True
            min_abs = min(min_abs, abs(n))

        if not zero and k % 2 == 1 :
            ans -= min_abs*2
        return ans
            
                
