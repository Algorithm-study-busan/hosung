cnt = [False for _ in range(1_000_001)]

def solution(elements):
    l = len(elements)
    
    for i in range(l) :
        total = 0
        for j in range(l) :
            total += elements[(i + j) % l]
            cnt[total] = True
            
    ans = 0
    for i in range(1_000_001) : 
        if cnt[i] :
            ans += 1
    
    return ans