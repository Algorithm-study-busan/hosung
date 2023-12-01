import heapq

class Node :
    a = 0
    b = 0
    c = 0
    
    def __init__(self, p) :
        self.a = p[0]
        self.b = p[1]
        self.c = p[2]
        
        
    def __lt__(self, other) :
        if self.a == other.a :
            return self.b < other.b 
        return self.a < other.a
    
    def __repr__(self) :
        return f"{self.a}, {self.b}, {self.c}"
        
        
def solution(program):
    ans = [0 for _ in range(11)]
    overtime = 0
    q = []
    
    program.sort(key = lambda x : [x[1], x[0]])
    
    for p in program :
        curtime = p[1]
        if curtime < overtime :
            heapq.heappush(q, Node(p))
        elif curtime == overtime :
            heapq.heappush(q, Node(p))
            x = heapq.heappop(q)
            ans[x.a] += x.b - overtime
            overtime += x.c
        else :
            while q and curtime > overtime :
                x = heapq.heappop(q)
                ans[x.a] += x.b - overtime
                overtime += x.c
            if curtime < overtime :
                heapq.heappush(q, Node(p))
            elif curtime == overtime :
                heapq.heappush(q, Node(p))
                x = heapq.heappop(q)
                ans[x.a] += x.b - overtime
                overtime += x.c
            else :
                overtime = curtime + p[2]
    
    while q :
        x = heapq.heappop(q)
        ans[x.a] += x.b - overtime
        overtime += x.c
    
    ans[0] = overtime
    return ans
                
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))