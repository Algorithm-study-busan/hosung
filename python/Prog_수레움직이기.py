def solution(a):
    cnt = [0 for _ in range(len(a) + 1)]
    last_idx = [-1 for _ in range(len(a) + 1)]
    
    if len(a) == 1 : return 0
    
    for i in range(len(a)) :
        if i != 0 and a[i] != a[i-1] and last_idx[a[i]] != i-1 :
            cnt[a[i]] += 1
            last_idx[a[i]] = i-1
        elif i < len(a) -1 and a[i] != a[i+1] :
            cnt[a[i]] += 1
            last_idx[a[i]] = i+1
    
    return max(cnt)*2