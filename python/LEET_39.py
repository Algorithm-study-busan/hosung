class Solution:
    def dfs(self, arr, idx, tmp, target, res) :
        if target == 0 : 
            res.append(tmp[:])
            return
        if idx == len(arr) or target < 0  : return

        self.dfs(arr, idx+1, tmp, target, res)
        for k in range(1, target//arr[idx] + 1) :
            tmp.append(arr[idx])
            self.dfs(arr, idx+1, tmp, target - arr[idx]*k, res)

        for k in range(1, target//arr[idx] + 1) :
            tmp.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        tmp = []
        res = []
        self.dfs(candidates, 0, tmp, target, res)
        return res
        