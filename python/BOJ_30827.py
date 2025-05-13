N,K = map(int, input().split())

arr = []

for _ in range(N) :
    a,b = map(int, input().split())
    arr.append([a,b])
    
times = [[-1,-1]] * K
    
arr.sort(key = lambda x : x[1])

ans = 0
for a,b in arr :
    idx = -1
    max_b = -2
    for i, time in enumerate(times) : 
        if time[1] < a and max_b < time[1] :
            idx = i
            max_b = time[1]
            
    if idx != -1 :
        times[idx] = [a,b]
        ans += 1
        
print(ans)