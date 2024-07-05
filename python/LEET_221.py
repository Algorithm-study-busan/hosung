class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        row = [[0 for _ in range(C+1)] for _ in range(R+1)]
        col = [[0 for _ in range(C+1)] for _ in range(R+1)]
        square = [[0 for _ in range(C+1)] for _ in range(R+1)]

        ans = 0
        for r in range(1, R+1) :
            for c in range(1, C+1) :
                if matrix[r-1][c-1] == '1' : 
                    row[r][c] = row[r-1][c]+1
                    col[r][c] = col[r][c-1]+1
                    square[r][c] = min(min(row[r][c], col[r][c]), square[r-1][c-1]+1)

                    ans = max(ans, square[r][c]**2)

        return ans

                
        