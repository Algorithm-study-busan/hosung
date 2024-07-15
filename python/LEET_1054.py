import heapq

pq = []
heapq.heappush(pq, [3,2])
heapq.heappush(pq, [2,2])


pq[1][0] = 1 
heapq.heappush(pq, [1,1])
print(pq)

print(heapq.heappop(pq))