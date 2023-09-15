import heapq

N = 0
K = 0
INF = 987654321

waiting_time = [ [0 for _ in range(21)] for _ in range(5) ]
times = [[] for _ in range(5)]
dp = [[[[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)] for _ in range(21)] for _ in range(21)]


def get_waiting_time(time, n) :
    pq = []
    ret = 0
    for s,d in time :
        while pq and pq[0] <= s :
            heapq.heappop(pq)
        
        if len(pq) < n :
            heapq.heappush(pq, s + d)
        else :
            first_out = heapq.heappop(pq)
            ret += first_out - s
            heapq.heappush(pq, first_out + d)
    return ret

def dfs(cnt, arr) :
    a,b,c,d,e = arr
    if dp[a][b][c][d][e] != -1 :
        return dp[a][b][c][d][e]
    
    if cnt == N :
        ret = 0
        for k in range(K) :
            ret += waiting_time[k][arr[k]]
        return ret
    
    ret = INF
    
    for k in range(K) :
        arr[k] += 1
        ret = min(ret, dfs(cnt+1, arr))
        arr[k] -= 1
    dp[a][b][c][d][e] = ret
    return ret

def solution(k, n, reqs):
    global N,K, waiting_time, times
    N = n 
    K = k 
    
    for a,b,c in reqs :
        times[c-1].append([a,b])
    
    for k in range(K) : 
        if times[k] :
            for n in range(1, n+1) :
                waiting_time[k][n] = get_waiting_time(times[k], n)
    
    return dfs(K, [1 for _ in range(5)])

    



    