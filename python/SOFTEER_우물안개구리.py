import sys

N, M = map(int, input().split())

w = list(map(int, input().split()))
f = [[] for _ in range(N+1)]

def is_best(n) :
    for ff in f[n] :
        if w[ff-1] >= w[n-1] : return False
    return True

for _ in range(M) :
    a,b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)


ans = 0
for n in range(1, N+1) :
    if is_best(n) : ans += 1

print(ans)

