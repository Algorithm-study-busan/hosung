class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check(idx) :
            if idx >= len(strs[0]) : return False
            c = strs[0][idx]

            for s in strs :
                if idx >= len(s) or s[idx] != c : return False

            return True

        ans = ""

        idx = 0
        while 1 :
            if check(idx) : idx += 1
            else : break
        return strs[0][:idx]

        
        