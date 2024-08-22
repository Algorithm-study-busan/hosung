from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        res = dict()

        q = deque()
        for i in range(len(values)) :
            a = equations[i][0]
            b = equations[i][1]
            c = values[i]

            res[(a,b)] = c 
            res[(b,a)] = 1/c
            q.append([a,b,c])
            q.append([b,a,1/c])
            edges[a].append([b,c])
            edges[b].append([a,1/c])

        while q :
            a,b,c = q.popleft()

            for nb, nc in edges[b] :
                x = c * nc
                if (a,nb) not in res :
                    res[(a, nb)] = x
                    q.append([a,nb,x])

        ans = []
        for a,b in queries :
            if (a,b) in res : ans.append(res[(a,b)])
            else : ans.append(-1)
        return ans

        



        