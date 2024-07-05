from functools import cmp_to_key

class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def cmp(o1, o2) : 
            if int(o1+o2) > int(o2+o1) : return -1
            else : return 1

        nums.sort(key = cmp_to_key(cmp))

        return str(int(''.join(nums)))
        
        