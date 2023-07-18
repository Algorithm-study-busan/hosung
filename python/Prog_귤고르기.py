from collections import defaultdict

def solution(K, tangerine):
    cnt = defaultdict(int)
    
    for t in tangerine :
        cnt[t] += 1
        
    arr = []
    for k, v in cnt.items() :
        arr.append([k,v])
        
    arr.sort(key = lambda x : -x[1])
    
    tmp = 0
    ans = 0
    for k,v in arr :
        tmp += v
        ans += 1
        
        print(ans, k)
        
        if tmp >= K : break
        
    return min(ans, K)
        
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))