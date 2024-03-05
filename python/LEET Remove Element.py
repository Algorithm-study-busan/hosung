class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []

        for n in nums :
            if n != val :
                arr.append(n)
                        
        nums[:] = arr
        return len(nums)