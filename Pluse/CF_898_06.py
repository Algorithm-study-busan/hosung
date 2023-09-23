from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T) :
    N,K = map(int, input().split())
    a_arr = list(map(int, input().split()))
    h_arr = list(map(int, input().split()))
    
    pfs = [0]
    for i in range(N) :
        pfs.append(pfs[-1] + a_arr[i])
    
    lo = 0
    hi = 0
    ans = 0
    while hi < N :
        if lo!=hi and h_arr[hi-1] % h_arr[hi] != 0 :
            lo = hi
        elif pfs[hi+1] - pfs[lo] > K :
            if lo == hi : hi += 1
            lo += 1
        else :
            ans = max(ans, hi-lo+1)
            hi += 1
    print(ans)