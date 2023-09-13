import heapq
import sys
sys.setrecursionlimit(1_000_000)

MAX = 100_000
INF = 987654321
cost = [[INF for _ in range(10)] for _ in range(10)]
dc = {
    1 : [[2,2], [4,2], [5,3]],
    2 : [[1,2], [3,2], [5,2], [4,3], [6,3]],
    3 : [[2,2], [6,2], [5,3]],
    4 : [[1,2], [5,2], [7,2], [2,3], [8,3]],
    5 : [[2,2], [4,2], [6,2], [8,2], [1,3], [3,3], [7,3], [9,3]], 
    6 : [[3,2], [5,2], [9,2], [2,3], [8,3]],
    7 : [[4,2], [8,2], [5,3], [0,3]],
    8 : [[5,2], [7,2], [9,2], [0,2], [4,3], [6,3]],
    9 : [[6,2], [8,2], [5,3], [0,3]],
    0 : [[8,2], [7,3], [9,3]]
}

nums = []
dp = [[[ -1 for _ in range(10)] for _ in range(10)] for _ in range(MAX+1)]

def dijkstra(s) :
    pq = []
    heapq.heappush(pq, s)
    cost[s][s] = 0
    while pq :
        cn = heapq.heappop(pq)
        
        for nn, k in dc[cn] :
            nc = cost[s][cn] + k
            if cost[s][nn] > nc :
                # 
                
                cost[s][nn] = nc
                heapq.heappush(pq, nn)
                
def find_cost() :
    for n in range(10) :
        dijkstra(n)
    for n in range(10) :
        cost[n][n] = 1
        

def find_dp(idx, l, r) :
    global dp
    if dp[idx][l][r] != -1 : return dp[idx][l][r]
    
    if l == r : return INF
    if idx == len(nums)-1 : return 0
    
    dp[idx][l][r] = min(find_dp(idx+1, nums[idx+1], r) + cost[l][nums[idx+1]],
                        find_dp(idx+1, l, nums[idx+1]) + cost[r][nums[idx+1]])

    return dp[idx][l][r]

def solution(numbers):
    global nums
    for c in numbers :
        nums.append(int(c))
        
    find_cost()
        
    return find_dp(-1, 4, 6)

