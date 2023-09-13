def get_next_idx(cap, idx, arr) :
    while idx >= 0 and cap > 0:
        x = min(arr[idx], cap)
        arr[idx] -= x
        cap -= x
        if arr[idx] == 0 : idx -= 1
        
    while idx >= 0 and arr[idx] == 0 :
        idx -= 1
    return idx

def solution(cap, n, deliveries, pickups):
    di = get_next_idx(0, n-1, deliveries)
    pi = get_next_idx(0, n-1, pickups)
    
    ans = 0
    while di >= 0 or pi >= 0 :
        ans += max(di+1, pi+1)*2
        di = get_next_idx(cap, di, deliveries)
        pi = get_next_idx(cap, pi, pickups)
        
    return ans