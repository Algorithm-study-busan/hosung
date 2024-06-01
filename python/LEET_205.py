class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char = dict()
        for i in range(len(s)) :
            if s[i] in char :
                if t[i] != char[s[i]] : return False
            else :
                if t[i] in char.values() : return False
                char[s[i]] = t[i]

        return True