class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = numRows
        if N == 1 : return s
        
        ans = ""

        for k in range(0,N) :
            for i in range(k,len(s), (N-1)*2) :
                ans += s[i] 
                mid_idx = i + 2*(N-1-k)
                if mid_idx < len(s) and mid_idx != i and mid_idx != i + (N-1)*2 :
                    ans += s[mid_idx]

        return ans

        