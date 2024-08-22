from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [ 0 for _ in range(numCourses) ]
        edges = [ [] for _ in range(numCourses) ]

        for a,b in prerequisites :
            inDegree[a] += 1
            edges[b].append(a)

        q = deque()
        ans = []
        for n in range(numCourses) :
            if inDegree[n] == 0 :
                q.append(n)

        while q :
            cur = q.popleft()
            ans.append(cur)

            for nxt in edges[cur] :
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0 :
                    q.append(nxt)

        if sum(inDegree) != 0 : return []
        return ans