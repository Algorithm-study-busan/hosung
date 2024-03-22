class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0
        idx = 0
        total = 1
        for i, x in enumerate(nums) :
            if x == 0 : 
                cnt += 1
                idx = i
            else :
                total *= x
        if cnt > 1 : return [0 for _ in range(len(nums))]
        if cnt == 1 : 
            ans = [0 for _ in range(len(nums))]
            ans[idx] = total
            return ans
        else :
            return [total // nums[i] for i in range(len(nums)) ]
        