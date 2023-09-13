MAX = 5_000_000
def solution(e, starts):
    cnt = [2 for _ in range(MAX+1)]
    cnt[1] = 1
    
    for a in range(2, e+1) :
        if a * a > MAX : break
        cnt[a*a] += 1
        for b in range(a+1, e+1) :
            if a * b > MAX : break
            cnt[a*b] += 2
            
    ans = [0 for _ in range(e+1)]
    tmp_max = 0
    tmp_n = 0
    for i in range(e, 0, -1) :
        if tmp_max <= cnt[i] : 
            tmp_max = cnt[i]
            tmp_n = i
        ans[i] = tmp_n
        
    return [ans[s] for s in starts]