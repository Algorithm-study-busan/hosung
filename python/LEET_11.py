class Solution:
    def maxArea(self, height: List[int]) -> int:
        li = 0
        ri = len(height)-1

        ans = 0
        while li < ri :
            ans = max(ans, (ri-li) * min(height[li], height[ri]))
            if height[li] < height[ri] :
                li += 1
            else :
                ri -= 1
        
        return ans
        