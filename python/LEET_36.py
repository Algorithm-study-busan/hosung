class Solution:
    def isValidCol(self, board, c) :
        checked = [False for _ in range(10)]
        
        for r in range(9) :
            if board[r][c] == '.' : continue
            n = int(board[r][c])
            if checked[n] : return False
            checked[n] = True
            
        return True
            
    def isValidRow(self, board, r) :
        checked = [False for _ in range(10)]
        
        for c in range(9) :
            if board[r][c] == '.' : continue
            n = int(board[r][c])
            if checked[n] : return False
            checked[n] = True
            
        return True
        
    def isValidBox(self, board, r, c) :
        checked = [False for _ in range(10)]
        for i in range(3) : 
            for j in range(3) :
                if board[r+i][c+j] == '.' : continue
                n = int(board[r+i][c+j])
                if checked[n] : return False
                checked[n] = True
            
        return True
                
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9) :
            if not self.isValidRow(board, r) : return False
        for c in range(9) :
            if not self.isValidCol(board, c) : return False
        for r in range(0,9,3) :
            for c in range(0,9,3) :
                if not self.isValidBox(board, r, c) : return False
        return True
        