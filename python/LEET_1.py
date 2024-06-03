class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i,x in enumerate(nums) :
            other = target - x
            if other in cache : 
                return [cache[other], i]
            else :
                cache[x] = i