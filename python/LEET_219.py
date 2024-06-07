class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        for i in range(min(len(nums), k+1)) :
            if nums[i] in check : return True
            check.add(nums[i])


        for i in range(k+1, len(nums)) :
            check.remove(nums[i-k-1])
            if nums[i] in check : return True
            check.add(nums[i])
            
        return False
        