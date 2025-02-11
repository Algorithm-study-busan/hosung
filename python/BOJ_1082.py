N = int(input())
P = list(map(int, input().split()))
M = int(input())

arr = []
for i,p in enumerate(P) :
    arr.append([i,p])
    
arr.sort(key=lambda x : [x[1], -x[0]])

if N == 1 or (arr[0][0] == 0 and arr[1][1] > M ) or (arr[0][0] != 0 and arr[0][1] > M) : 
    print(0)
else : 
    ans = ""
    if arr[0][0] == 0 :
        ans += str(arr[1][0])
        M -= arr[1][1]
    else :
        ans += str(arr[0][0])
        M -= arr[0][1]
    
    while M-arr[0][1] >= 0 :
        ans += str(arr[0][0])
        M -= arr[0][1]
    
    arr.sort(key = lambda x : [-x[0], x[1]])
    opt_ans = ""
    for c in ans :
        ck = False
        for i,p in arr :
            if int(c) < i and  p-P[int(c)] <= M : 
                M -= p-P[int(c)]
                opt_ans += str(i)
                ck = True
                break
        if not ck : 
            opt_ans += c
            
    print(opt_ans)
    
    