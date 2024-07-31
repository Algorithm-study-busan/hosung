class Solution:
    
    def binarySearch(self, arr, lo, hi, target) :
        tmp = lo
        while lo <= hi :
            mid = (lo + hi)//2
            if arr[mid] < target : lo = mid+1
            else : hi = mid-1
        
        return lo - tmp

    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)) :
                ans += self.binarySearch(nums, j+1, len(nums)-1, nums[i]+nums[j])
        return ans
