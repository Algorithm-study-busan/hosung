N,M = map(int, input().split())
arr = list(map(int, input().split()))

INF = 987654321

def count_arr(arr, size) :
    tmp = 0
    res = 1
    for a in arr :
        if a > size : return INF
        if a + tmp <= size :
            tmp += a
        else :
            res += 1
            tmp = a
    return res
        

lo = 1
hi = sum(arr)

while lo <= hi :
    mid = (lo + hi) // 2
    if count_arr(arr, mid) < M :
        hi = mid-1
    elif count_arr(arr, mid) > M :
        lo = mid+1
    else :
        hi = mid-1
print(lo)