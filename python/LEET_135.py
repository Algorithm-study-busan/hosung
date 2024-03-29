class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1 for _ in range(len(ratings))]
        arr = []
        for i, x in enumerate(ratings) :
            arr.append([x, i])
        arr.sort()
        
        for x, i in arr :
            if i-1 >= 0 and ratings[i-1] < ratings[i] :
                ans[i] = max(ans[i], ans[i-1]+1)
            if i+1 < len(ans) and ratings[i+1] < ratings[i] :
                ans[i] = max(ans[i], ans[i+1]+1)
        
        return sum(ans)


        