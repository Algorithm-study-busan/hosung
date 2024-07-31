class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo = 1
        hi = m*n

        while lo <= hi :
            mid = (lo + hi)//2

            tmp = 0
            for r in range(1, m+1) :
                tmp += min(n, mid // r)
            
            if k <= tmp : hi = mid-1
            elif k > tmp : lo = mid+1
        return lo