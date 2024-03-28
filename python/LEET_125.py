class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''
        for c in s :
            if c.isalnum() :
                p += c.lower()
        for i in range(len(p)//2) : 
            if p[i] != p[len(p)-1-i] : return False
        return True
