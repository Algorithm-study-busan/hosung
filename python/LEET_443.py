from collections import deque

class Solution:
    def valid(self, g1, g2) :
        cnt = 0
        for i in range(8) :
            if g1[i] != g2[i] : cnt += 1
        return cnt == 1
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([[0,startGene]])
        visited = [False for _ in range(len(bank))]
        while q : 
            cnt, cur = q.popleft()
            if cur == endGene : 
                return cnt
            for i, nxt in enumerate(bank) :
                if not visited[i] and self.valid(cur, nxt) :
                    visited[i] = True
                    q.append([cnt+1, nxt])
        return -1
                    
            
        