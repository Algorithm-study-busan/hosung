class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)) :
            num += digits[len(digits)-1-i] * 10**i
        
        ans = []

        for c in str(num+1) : ans.append(int(c))

        return ans
        
        