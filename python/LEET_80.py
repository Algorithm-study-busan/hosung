class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)) :
            if i >=2 and nums[i] == nums[i-1] and nums[i] == nums[i-2] :
                continue
            res.append(nums[i])
        nums[:] = res
        return len(nums)
        