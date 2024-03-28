class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I' : 1,
            "V" : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans = 0
        i = 0
        while i < len(s)  :
            if i < len(s)-1 and nums[s[i]] < nums[s[i+1]] :
                ans += nums[s[i+1]] - nums[s[i]]
                i += 2
            else :
                ans += nums[s[i]]
                i += 1
        return ans