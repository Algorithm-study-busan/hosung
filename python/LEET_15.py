class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        nums_set = []

        for i in range(len(nums)) :
            if i > 2 and nums[i] == nums[i-1] == nums[i-2] == nums[i-3]: continue
            nums_set.append(nums[i])
        
        for i in range(len(nums_set)-2) :
            l = i+1
            r = len(nums_set)-1
            
            k = -nums_set[i]

            while l < r :
                if nums_set[l] + nums_set[r] < k :
                    l += 1
                elif nums_set[l] + nums_set[r] > k :
                    r -= 1
                else :
                    ans.append([nums_set[i], nums_set[l], nums_set[r]])
                    l += 1
                    r -= 1
        
        ans.sort()
        ans_set = []

        for i in range(len(ans)) :
            if i > 0 and ans[i] == ans[i-1] : continue 
            ans_set.append(ans[i])
        return ans_set