class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        row = [False for _ in range(R)]
        col = [False for _ in range(C)]

        for r in range(R) :
            for c in range(C) :
                if matrix[r][c] == 0 :
                    row[r] = True
                    col[c] = True

        for r in range(R) :
            if row[r] :
                for c in range(C) :
                    matrix[r][c] = 0
            
        for c in range(C) :
            if col[c] :
                for r in range(R) :
                    matrix[r][c] = 0

        
        