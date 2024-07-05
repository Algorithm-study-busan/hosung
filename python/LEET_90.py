class Solution:
    def dfs(self, nums, idx, tmp, ans) :
        if idx == len(nums) : 
            ans.append(tmp[:])
            return
        tmp.append(nums[idx])
        self.dfs(nums, idx+1, tmp, ans)
        tmp.pop()

        next_idx = idx+1
        while next_idx < len(nums) and nums[next_idx] == nums[next_idx-1] :
            next_idx += 1
        self.dfs(nums, next_idx, tmp, ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        tmp = []
        ans = []
        self.dfs(nums, 0, tmp, ans)
        return ans
            
        