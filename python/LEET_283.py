class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans = []
        for n in nums : 
            if n == 0 : continue
            ans.append(n)

        for _ in range(len(nums)-len(ans)) :
            ans.append(0)
        
        nums[:] = ans
        