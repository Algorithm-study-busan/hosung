class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k]) / k
        tmp = ans
        for i in range(k, len(nums)) :
            tmp += nums[i] / k
            tmp -= nums[i-k] / k
            ans = max(ans, tmp)
        return ans
        