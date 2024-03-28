class Solution:
    def trap(self, height: List[int]) -> int:
        left_sum = 0
        max_height = 0
        for h in height :
            max_height = max(max_height, h)
            left_sum += max_height - h
        
        right_sum = 0
        max_height = 0
        for h in height[::-1] :
            max_height = max(max_height, h)
            right_sum += max_height - h
        
        total_sum = 0
        for h in height :
            total_sum += max_height - h
        
        return left_sum + right_sum - total_sum

        