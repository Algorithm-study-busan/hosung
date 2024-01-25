N = int(input())

arr = list(map(float, input().split()))
    
if N == 1 :
    print(arr[0])
else :
    ans = 0
    ans += arr[0]*2
    ans += arr[N-1]*2
    
    for i in range(1,N-1) :
        ans += arr[i]*3
        ans -= (arr[i]*arr[i-1])*2 
        
    ans -= (arr[N-1]*arr[N-2])*2
    print(ans)