class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows) :
            arr = []
            for k in range(i+1) :
                if k == 0 or k == i : arr.append(1)
                else : arr.append(ans[i-1][k-1] + ans[i-1][k])
            ans.append(arr)

        return ans
        