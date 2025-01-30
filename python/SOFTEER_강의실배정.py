import sys

N = int(input())

arr = []

for _ in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort(key = lambda x : x[1])

ans = 0
last = -1

for a,b in arr :
    if a >= last : 
        last = b
        ans += 1

print(ans)