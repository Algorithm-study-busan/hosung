def solution(land, P, Q):
    arr = []
    
    for row in land :
        arr.extend(row)
        
    arr.sort()
    N = len(arr)
    
    temp = (sum(arr) - arr[0]*N) * Q
    ans = temp
    
    for i in range(1, len(arr)) :
        down = i
        up = N-i
        
        temp += down * (arr[i]-arr[i-1]) * P
        temp -= up * (arr[i]-arr[i-1]) * Q
        
        ans = min(ans,temp)
        
    return ans
        
    