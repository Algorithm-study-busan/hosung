from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)

        visited = [False for _ in range(N)]

        ans = 0
        for n in range(N) :
            if visited[n] : continue
            ans += 1
            q = deque([n])
            visited[n] = True
            while q :
                cur = q.popleft()
                for nxt in range(N) :
                    if not isConnected[cur][nxt] or visited[nxt]: continue
                    visited[nxt] = True
                    q.append(nxt)
        return ans
        