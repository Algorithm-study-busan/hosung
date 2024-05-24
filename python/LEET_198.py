class Solution:
    def __init__(self) :
        self.dp = [[-1 for _ in range(2)] for _ in range(101)]

    def find_dp(self, nums, idx, k) :
        if idx == 0 :
            if k == 0 : return 0
            if k == 1 : return nums[0]
        
        if self.dp[idx][k] != -1 : return self.dp[idx][k]
        if k == 1 : 
            self.dp[idx][k] = nums[idx] + self.find_dp(nums, idx-1, 0)
        else :
            self.dp[idx][k] = max(self.find_dp(nums, idx-1, 0), self.find_dp(nums, idx-1, 1))
        return self.dp[idx][k]
    def rob(self, nums: List[int]) -> int:
        return max(self.find_dp(nums, len(nums)-1, 0), self.find_dp(nums, len(nums)-1, 1))