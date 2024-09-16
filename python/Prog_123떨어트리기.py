import math

def solution(edges, target):
    N = len(edges)+1
    e = [[] for _ in range(N+1)]
    idx = [0 for _ in range(N+1)]
    
    for a,b in edges :
        e[a].append(b)
        
    for arr in e :
        arr.sort()
        
    def move(cur) :
        if not e[cur] : return cur
        
        nxt = e[cur][idx[cur]]
        idx[cur] = (idx[cur]+1) % len(e[cur])
        
        return move(nxt)
    
    cnt = [0 for _ in range(N+1)]
    
    def allClear() :
        for n in range(1,N+1) :
            if cnt[n] != 0 or target[n-1] != 0 :
                if cnt[n] < target[n-1] / 3 or cnt[n] > target[n-1] : return False
        return True
                
    
    while True :
        node = move(1)
        cnt[node] += 1
        if target[node-1] < cnt[node] : return [-1]
        if allClear() : break
    
    idx = [0 for _ in range(N+1)]
    
    ans = []
    for _ in range(sum(cnt)) :
        node = move(1)
        for x in range(1,4) :
            if cnt[node]-1 >= (target[node-1] - x) / 3 :  
                target[node-1] -= x
                cnt[node]-=1
                ans.append(x)
                break
    return ans
        
        
    