N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False for _ in range(N)]

result = []

def is_equal(arr1, arr2) :
    if len(arr1) != len(arr2) : return False
    for i in range(len(arr1)) :
        if arr1[i] != arr2[i] : return False
    return True

def f() :
    if len(result) == M :
        print(*result)
        return
        
    prev = 0
    for i in range(N) :
        if visited[i] or prev == arr[i] : continue 
        prev = arr[i]
        visited[i] = True
        result.append(arr[i])
        f()
        visited[i] = False
        result.pop()
        
    
f()