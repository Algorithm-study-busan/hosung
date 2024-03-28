class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        while si < len(s) and ti < len(t) :
            if s[si] != t[ti] : 
                ti += 1
            else :
                si += 1
                ti += 1
        if si == len(s) : return True
        else : return False