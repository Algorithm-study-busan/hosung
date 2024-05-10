class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi :
            if nums[lo] > nums[hi] :
                mid = (lo + hi) // 2
                if nums[mid] >= nums[lo] :
                    lo = mid + 1
                else :
                    hi = mid
            else :
                return nums[lo]
        return nums[lo]
        