class Solution:

    def reverse(self, arr, start, end) :
        for i in range((end-start+1)//2) :
            arr[start+i], arr[end-i] = arr[end-i], arr[start+i]


    def nextPermutation(self, nums: List[int]) -> None:
        idx = len(nums)-1
        while idx > 0 and nums[idx-1] >= nums[idx]  :
            idx -= 1
            
        self.reverse(nums, idx, len(nums)-1)
        if idx == 0 : return 
    
        for i in range(idx, len(nums)) :
            if nums[i] > nums[idx-1] :
                nums[i], nums[idx-1] = nums[idx-1], nums[i]
                return

        