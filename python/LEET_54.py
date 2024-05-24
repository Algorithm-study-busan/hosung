class Solution:
    def appendFrame(self, sr, sc, er, ec, matrix, arr) :
        if sr == er and sc == ec :
            arr.append(matrix[sr][sc])
            return

        if sr == er :
            for c in range(sc, ec+1) :
                arr.append(matrix[sr][c])
            return
        
        if sc == ec :
            for r in range(sr, er+1) :
                arr.append(matrix[r][sc])
            return
            
        for c in range(sc, ec) :
            arr.append(matrix[sr][c])
        for r in range(sr, er) :
            arr.append(matrix[r][ec])
        for c in range (ec, sc, -1) :
            arr.append(matrix[er][c])
        for r in range(er, sr, -1) :
            arr.append(matrix[r][sc])
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sr = 0
        sc = 0
        er = len(matrix)-1
        ec = len(matrix[0])-1
        
        arr = []
        
        while sr <= er and sc <= ec :
            self.appendFrame(sr, sc, er, ec, matrix, arr)
            sr += 1
            sc += 1
            er -= 1
            ec -= 1
            
        return arr