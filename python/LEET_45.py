class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        final = 0
        cnt = 0
        for i in range(len(nums)-1) :
            reach = max(reach, i+nums[i])
            if i == final :
                final = reach
                cnt += 1
        return cnt