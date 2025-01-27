import sys

N = int(input())
arr = list(map(int, input().split()))

dp_left = [0] * N
dp_right = [0] * N


dp_left[0] = arr[0]
dp_right[N-1] = arr[N-1]

tmp = dp_left[0]
for i in range(1, N) :
    if tmp < 0 :
        tmp = arr[i]
    else :
        tmp += arr[i]
    dp_left[i] = max(tmp, dp_left[i-1])

tmp = dp_right[N-1]
for i in range(N-2, -1,-1) :
    if tmp < 0 :
        tmp = arr[i]
    else :
        tmp += arr[i]
    dp_right[i] = max(tmp, dp_right[i+1])

ans = -9876543210

for i in range(1, N-1) :
    ans = max(ans, dp_left[i-1] + dp_right[i+1])
print(ans)
