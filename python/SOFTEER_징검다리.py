import sys

N = int(input())
arr = list(map(int, input().split()))

dp = []

def bs(val) :
    lo = 0
    hi = len(dp)-1

    while lo <= hi :
        mid = (lo+hi)//2
        if dp[mid] < val : lo = mid+1
        else : hi = mid-1

    return lo

for n in arr :
    if not dp :
        dp.append(n)
    else :
        idx = bs(n)
        if idx == len(dp) :
            dp.append(n)
        else :
            dp[idx] = n

print(len(dp))
    