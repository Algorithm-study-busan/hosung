class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi :
            mid = (lo + hi)//2
            if n < mid*(mid+1)//2 : hi = mid-1
            elif n > mid*(mid+1)//2 : lo = mid+1
            else : return mid
        return lo-1


        