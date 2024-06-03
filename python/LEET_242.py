from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in s :
            s_dict[c] += 1

        for c in t :
            if c not in s_dict or s_dict[c] <= 0 : return False
            s_dict[c] -= 1 

        for cnt in s_dict.values() : 
            if cnt > 0 : return False
        
        return True

        
        