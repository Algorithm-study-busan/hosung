
def solve(arr, copy) :
    for i in range(len(arr)) :
        if arr[i] % 2 != copy[i] %2 : 
            print("NO")
            return
    print("YES")
    

T =  int(input())
for _ in range(T) :
    n = int(input())
    arr = list(map(int, input().split()))
    copy = arr[:]
    copy.sort()
    solve(arr,copy)
    
            
    
    