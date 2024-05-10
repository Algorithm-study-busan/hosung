class Solution:
    def lower_bound(self, nums, target) :
        lo = 0
        hi = len(nums)-1

        while lo<=hi :
            mid = (lo + hi)//2
            if nums[mid] < target :
                lo = mid + 1
            elif nums[mid] >= target : 
                hi = mid - 1
        return lo
                


    def upper_bound(self, nums, target) :
        lo = 0
        hi = len(nums)-1

        while lo<=hi :
            mid = (lo + hi)//2
            if nums[mid] <= target :
                lo = mid + 1
            elif nums[mid] > target : 
                hi = mid - 1
        return lo
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums : return [-1,-1]
        l = self.lower_bound(nums, target)
        if l == len(nums) or nums[l] != target: 
            return[-1,-1]
        r = self.upper_bound(nums, target)
        return [l, r-1]
        