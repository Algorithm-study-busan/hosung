class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x

        while lo < hi :
            mid = (lo + hi)//2
            if mid**2 <= x : lo = mid+1
            else : hi = mid
        if lo * lo == x : return lo
        else : return lo-1
        