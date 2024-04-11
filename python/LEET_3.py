class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set = set()
        left = 0
        ans = 0

        for i,c in enumerate(s) :
            if c in substring_set : 
                while s[left] != c :
                    substring_set.remove(s[left])
                    left += 1
                substring_set.remove(s[left])
                left += 1

            substring_set.add(c)
            ans = max(ans, i-left+1)
        
        return ans
        