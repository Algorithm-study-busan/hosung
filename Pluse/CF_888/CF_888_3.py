from sys import stdin
input = stdin.readline

def count(arr,k):
    x = arr[0]
    y = arr[-1]
    if x ==  y :
        if arr.count(x) >= k :
            print("YES")
        else :
            print("NO")
        return
    cnt_x = 0
    cnt_y = 0
    
    lo = 0
    hi = len(arr)-1
    
    while lo <= hi :
        if arr[lo] == x :
            cnt_x += 1
        if arr[hi] == y : 
            cnt_y += 1
        
        if cnt_x >= k and cnt_y >= k : 
            print("YES")
            return
        if cnt_x < k : lo += 1
        if cnt_y < k : hi -= 1
    print("NO")

T = int(input())
for _ in range(T) :
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count(arr, k)