class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        
        tmp = [[0 for _ in range(n)] for _ in range(n)]

        for c in range(n) :
            for r in range(n-1,-1,-1) :
                nr = i // n
                nc = i % n
                tmp[nr][nc] = matrix[r][c]
                i += 1
                
        for r in range(n) :
            for c in range(n) :
                matrix[r][c] = tmp[r][c]
                
