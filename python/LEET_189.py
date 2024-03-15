class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        res = []
        for i in range(len(nums)-k, len(nums)) :
            res.append(nums[i])
        for i in range(len(nums)-k) :
            res.append(nums[i])
        nums[:] = res 

        