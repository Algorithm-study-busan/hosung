class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        ans = 0
        while nums_set :
            n = nums_set.pop()

            lo = n-1
            while lo in nums_set :
                nums_set.remove(lo)
                lo -= 1

            hi = n+1
            while hi in nums_set :
                nums_set.remove(hi)
                hi += 1
            
            ans = max(ans, hi-lo-1)

        return ans