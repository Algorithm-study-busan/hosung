N = 0
dp_min = [[]]
dp_max = [[]]

def cal(arr, l, r) :
    ret = int(arr[l+1])
    for i in range(l+3, r+1, 2) :
        if arr[i-1] == '+' : ret += int(arr[i])
        else : ret -= int(arr[i])
    
    if arr[l] == '-' : return -ret
    return ret

def find_dp(arr, l, r, check) :
    if r-l == 1 : return cal(arr, l, r)
    
    if arr[l] == '-' : check = not check
    ret = cal(arr, l, r)
    if check : 
        for i in range(l+1, r, 2) :
            ret = max(ret, find_dp(arr,l, i, check) + find_dp(arr, i+1, r, check))
            
        
    else : 
        for i in range(l+1, r, 2) :
            ret = min(ret, find_dp(arr,l, i, check) + find_dp(arr, i+1, r, check))
            
    return ret

    
        

def solution(arr):
    global N, dp_min, dp_max
    arr.insert(0, '+')
    N = len(arr)
    dp_min = [[-1 for _ in range(N)] for _ in range(N)]
    dp_max = [[-1 for _ in range(N)] for _ in range(N)]
    
    return find_dp(arr,0,N-1, True)
    
    
print(solution(["1", "-", "3", "+", "5", "-", "8"]))
    
    
    
    
    
    