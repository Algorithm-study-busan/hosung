class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = dict()
        arr = s.split()

        if len(pattern) != len(arr) : return False

        for i in range(len(pattern)) :
            if pattern[i] in mapping :
                if arr[i] != mapping[pattern[i]] : return False
            else :
                if arr[i] in mapping.values() : return False
                mapping[pattern[i]] = arr[i]
        return True 
        