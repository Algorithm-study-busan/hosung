class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0

        lo = 0
        hi = len(nums)-1
        while lo < hi :
            if nums[lo] + nums[hi] < k :
                lo += 1
            elif nums[lo] + nums[hi] > k :
                hi -= 1
            else :
                ans += 1
                lo += 1
                hi -= 1
        return ans

        