from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_cnt = defaultdict(int)

        for r in range(len(grid)) : 
            row_cnt[tuple(grid[r])] += 1

        ans = 0
        for c in range(len(grid)) :
            col = []
            for r in range(len(grid)) :
                col.append(grid[r][c])
            ans += row_cnt[tuple(col)]
        return ans