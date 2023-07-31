import heapq

N = 0
K = 0

waiting_time = [ [0 for _ in range(21)] for _ in range(5) ]
times = [[] for _ in range(5)]

# def get_waiting_time(time, n) :
#     pq = []
#     for s,d in time :
#         while pq and heapq.
    

def solution(k, n, reqs):
    global N,K, waiting_time, times
    N = n 
    K = k 
    
    for a,b,c in reqs :
        times[c-1].append([a,b])
    
    
pq = [3,1,2]
print(heapq.nlargest(pq))
print(heapq.nsmallest(pq))


    