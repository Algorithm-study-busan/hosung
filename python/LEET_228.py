class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums : return []
        start = nums[0]
        ans = []
        for i in range(1, len(nums)) :
            if nums[i-1] == nums[i]-1 : continue
            elif nums[i-1] != nums[i]-1 :
                if start == nums[i-1] : 
                    ans.append(f"{start}")
                else : 
                    ans.append(f"{start}->{nums[i-1]}")
                start = nums[i]

        if start == nums[-1] : 
            ans.append(f"{start}")
        else :
            ans.append(f"{start}->{nums[-1]}")
        return ans



        