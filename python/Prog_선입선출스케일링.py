def cal_end_work(time, cores) :
    ret = 0
    for core in cores :
        ret += time // core + 1
    return ret

def solution(n, cores):
    lo = 0
    hi = 500_000_000
    
    while lo <= hi :
        mid = (lo + hi) // 2
        if cal_end_work(mid, cores) >= n : hi = mid-1
        else : lo = mid+1
    
    if cal_end_work(lo, cores) < n : lo += 1
    
    arr = []
    for i, core in enumerate(cores) :
        if lo % core == 0 : arr.append(i+1)
    
    return arr[-1 -(cal_end_work(lo, cores) - n)]