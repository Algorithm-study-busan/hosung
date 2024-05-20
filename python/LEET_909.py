from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        for i in range(len(board)) :
            if i % 2 == 1 : 
                board[i] = board[i][::-1]
                
        n = len(board)
        
        visited = [-1 for _ in range(n*n)]
        visited[0] = 0
        q = deque([0])
    
        while q :
            cur = q.popleft()
            if cur == n*n-1 :
                return visited[cur]
                
            for i in range(1, 7) :
                nxt = min(n*n-1, cur+i)
                if board[nxt//n][nxt%n] > 0 :
                    nxt = board[nxt//n][nxt%n]-1
                if visited[nxt] == -1 :
                    visited[nxt] = visited[cur]+1
                    q.append(nxt)
                    
        return -1
                
                
            
        