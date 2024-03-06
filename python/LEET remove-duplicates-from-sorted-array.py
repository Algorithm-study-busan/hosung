class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = list(set(nums))
        nums[:] = sorted(res)
        return len(res)
        