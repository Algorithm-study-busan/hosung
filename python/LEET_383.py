from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int) 
        for c in magazine : 
            count[c] += 1

        for c in ransomNote :
            if count[c] - 1 < 0 : return False
            count[c] -= 1
        
        return True
        