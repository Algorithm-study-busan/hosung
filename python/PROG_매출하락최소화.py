def solution(sales, links):
    dp = [[-1 for _ in range(2)] for _ in range(300001)]
    edges = [[] for _ in range(300001)]
    
    for a,b in links :
        edges[a].append(b)
    
    def dfs(cur, k) :
        if dp[cur][k] != -1 : return dp[cur][k]
        dp[cur][k] = 0
        
        tmp = []
        for nxt in edges[cur] :
            tmp.append([dfs(nxt, 0), dfs(nxt,1)])
        
        if k == 1 :
            dp[cur][k] += sales[cur-1]
            for k0, k1 in tmp :
                dp[cur][k] += min(k0,k1)
                
        else :
            tmp_k_min = 987654321
            for i in range(len(tmp)) :
                tmp_k = tmp[i][1]
                for j in range(len(tmp)) :
                    if j == i : continue
                    tmp_k += min(tmp[j][0], tmp[j][1])
                tmp_k_min = min(tmp_k_min, tmp_k)
            if tmp_k_min != 987654321 : dp[cur][k] = tmp_k_min
        return dp[cur][k]
    return min(dfs(1,0), dfs(1,1))
                
        