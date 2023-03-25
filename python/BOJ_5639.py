import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

arr = []

while True :
    try :
        x = int(input())
        arr.append(x)
    except :
        break
    
def find_mi(si, ei) :
    for i in range(si, ei+1) :
        if arr[i] > arr[si] : return i-1
    return ei
    
def dfs(si, ei) :
    if si > ei : return
    mi = find_mi(si, ei)
    dfs(si+1, mi)
    dfs(mi+1, ei)
    print(arr[si])
    
print(dfs(0, len(arr)-1))