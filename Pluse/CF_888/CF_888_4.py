T = int(input())

for _ in range(T) :
    n = int(input())
    arr = list(map(int, input().split()))
    check = [False for _ in range(n+1)]
    origin = []
    origin.append(arr[0])
    for i in range(1, len(arr)) :
        origin.append(arr[i]-arr[i-1])
    
    num = -1
    cnt = 0
    for x in origin :
        if x > n or x <= 0 or check[x] :
            num = x
            cnt += 1
        if x <= n :
            check[x] = True
        
    missing_num = 0
    for x in range(1, n+1) :
        if not check[x] : missing_num += x
    
    if cnt > 1 : 
        print("NO")
    elif num == -1 or num == missing_num :
        print("YES")
    else :
        print("NO")