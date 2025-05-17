S = input()

arr = []
for c in S :
    if c == '_' :
        arr.append(-1)
    elif c == 'L' : 
        arr.append(2)
    elif c in {'A', 'E', 'I', 'O', 'U'} : 
        arr.append(1)
    else :
        arr.append(0)
        
mul = [20, 5, 1]

ans = 0

def isGood(arr) :
    ck_L = False
    for n in arr[:2] :
        if n == 2 : ck_L = True
    for i in range(2, len(arr)) :
        if arr[i] == 2 : ck_L = True
        if arr[i]%2 == arr[i-1]%2 == arr[i-2]%2 : return False
    
    return ck_L
        
def dfs(arr, idx, tmp) :
    global ans
    if idx == len(arr) :
        if isGood(arr) :
            ans += tmp 
        return
    if arr[idx] != -1 : return dfs(arr, idx+1, tmp)
    for i in range(3) :
        arr[idx] = i
        dfs(arr, idx+1, tmp * mul[i])
    arr[idx] = -1
    
dfs(arr, 0, 1)
print(ans)
    
    
    