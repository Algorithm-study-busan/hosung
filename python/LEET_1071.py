class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDiviable(ss, s) :
            if len(ss) % len(s) != 0 : return False
            return s * (len(ss) // len(s)) == ss
        ans = ""
        for i in range(min(len(str1), len(str2))) :
            s = str1[:i+1]
            if isDiviable(str1, s) and isDiviable(str2, s) :
                ans = s
        
        return ans


        