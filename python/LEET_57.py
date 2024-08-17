class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ck = True
        for a, b in intervals :
            if newInterval[0] <= a <= newInterval[1] or newInterval[0] <= b <= newInterval[1] or a <= newInterval[0] <= b or a <= newInterval[1] <= b:
                newInterval[0] = min(newInterval[0], a)
                newInterval[1] = max(newInterval[1], b)
            elif newInterval[1] < a and ck:
                ans.append(newInterval)
                ans.append([a,b])
                ck = False
            else :
                ans.append([a,b])
        if len(ans) == 0 or ans[-1][1] < newInterval[0] :
            ans.append(newInterval)
        return ans
        