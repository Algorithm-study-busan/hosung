from collections import deque

class Solution:

    def bfs(self, r,c, board, visited) :
        dr = [-1,0,1,0]
        dc = [0,-1,0,1]
        R = len(board)
        C = len(board[0])

        q = deque([[r,c]])
        visited[r][c] = True
        surrounded = True

        tmp = []

        while q :
            cr, cc = q.popleft()
            tmp.append([cr, cc])
            for i in range(4) :
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0<=nr<R and 0<=nc<C : 
                    if board[nr][nc] == 'O' and not visited[nr][nc] : 
                        q.append([nr,nc])
                        visited[nr][nc] = True
                else :
                    surrounded = False

        if surrounded :
            for r, c in tmp :
                board[r][c] = 'X'
        

    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        visited = [[False for _ in range(C)] for _ in range(R)]

        for r in range(R) :
            for c in range(C) :
                if board[r][c] == 'O' and not visited[r][c] :
                    self.bfs(r, c, board, visited)
        