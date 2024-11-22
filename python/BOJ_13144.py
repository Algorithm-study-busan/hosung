N = int(input())
arr = list(map(int, input().split()))

d = dict()

idx = 0
ans = 0
for i,n in enumerate(arr) :
    if n in d and d[n] >= idx:
        idx = d[n]+1
    
    d[n] = i
    ans += i-idx+1
    
print(ans)