class Solution:
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    def count_board(self, board, r, c) :
        R = len(board)
        C = len(board[0])

        cnt = 0
        for i in range(8) :
            nr = r + self.dr[i]
            nc = c + self.dc[i]
            if 0<=nr<R and 0<=nc<C and board[nr][nc] == 1:
                cnt += 1
        return cnt

        

    def gameOfLife(self, board: List[List[int]]) -> None:
        R = len(board)
        C = len(board[0])

        nxt = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R) :
            for c in range(C) :
                cnt = self.count_board(board, r, c)
                if board[r][c] == 1 :
                    if cnt == 2 or cnt == 3 : 
                        nxt[r][c] = 1
                else :
                    if cnt == 3 : nxt[r][c] = 1

        for r in range(R) :
            for c in range(C) :
                board[r][c] = nxt[r][c]