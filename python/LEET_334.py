class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 9876543210
        second = 9876543210

        for n in nums :
            if n <= first :
                first = n
            elif n <= second :
                second = n
            else :
                return True
        return False
            
        