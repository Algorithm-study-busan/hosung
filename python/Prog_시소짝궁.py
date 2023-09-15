def lower_bound(lo, hi, arr, x) :
    while lo <= hi :
        mid = (lo + hi)//2
        if arr[mid] < x :
            lo = mid+1
        else :
            hi = mid-1
    return lo
            
def upper_bound(lo, hi, arr, x) :
    while lo<=hi :
        mid = (lo + hi)//2 
        if arr[mid] <= x :
            lo = mid+1
        else :
            hi = mid-1
    return lo

def count(lo,hi,arr, x):
    return upper_bound(lo,hi,arr,x) - lower_bound(lo,hi,arr,x)

def solution(weights):
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    weights.sort()
    for w in weights :
        w1.append(w)
        w2.append(w*2)
        w3.append(w*3)
        w4.append(w*4)
    
    ans = 0
    for i in range(1, len(weights)) :
        w = weights[i]
        ans += count(0, i-1, w1, w)
        ans += count(0, i-1, w3, 2*w)
        ans += count(0, i-1, w4, 2*w)
        ans += count(0, i-1, w4, 3*w)
    
    return ans
        
        
        
        
arr = [1,1,2,2,3,3]

        
    