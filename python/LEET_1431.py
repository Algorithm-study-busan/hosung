class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_n = max(candies)
        ans = []
        for can in candies :
            if can + extraCandies >= max_n :
                ans.append(True)
            else :
                ans.append(False)
        return ans
        