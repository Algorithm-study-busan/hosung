import heapq

INF = 987654321

q = []
heapq.heappush(q, [2,3])
heapq.heappush(q, [5,3])
heapq.heappush(q, [3,4])

print(heapq.heappop(q))