from collections import defaultdict

cnt = defaultdict(int)

N = int(input())
arr = list(map(int, input().split()))

ans = 0
for n in arr :
    if cnt[n+1] > 0 :
        cnt[n+1] -= 1
        cnt[n] += 1
    else :
        cnt[n] += 1
        ans += 1

print(ans)
