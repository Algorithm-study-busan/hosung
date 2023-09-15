import heapq

def solution(n, k, enemy):
    ans = 0
    pq = []
    
    for e in enemy :
        heapq.heappush(pq, -e)
        if n < e :
            if k == 0 : break
            n += -heapq.heappop(pq)
        ans += 1
        n -= e
        heapq.heappush(pq, -e)
    return ans




        
            

