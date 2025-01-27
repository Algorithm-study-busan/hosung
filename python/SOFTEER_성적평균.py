import sys

pSum = [0]
tmp = 0

N,K = map(int, input().split())
arr = list(map(int, input().split()))

for n in arr :
    tmp += n
    pSum.append(tmp)

for _ in range(K) :
    a,b = map(int,input().split())
    ans = (pSum[b] - pSum[a-1]) / (b-a+1)
    ans = round(ans, 2)
    print(f"{ans:.2f}")