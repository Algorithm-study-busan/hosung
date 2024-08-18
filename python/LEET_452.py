class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])

        end = points[0][1]

        ans = 1
        for s, e in points[1:] :
            if s<=end : continue
            else :
                ans += 1
                end = e
        return ans
    
# 2 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def isOverlap(points, a, b) :
            if len(points) == 0 : return False
            c,d = points[-1]
            if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b :
                return True

        points.sort()

        ans = 0
        while points :
            ans += 1
            a,b = points.pop()
            while isOverlap(points, a,b) :
                c, d = points[-1]
                a = max(a, c)
                b = min(b, d)
                points.pop()

        return ans