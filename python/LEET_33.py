arr = [1,2,3,3,3,4,5]
target = 3

def binary_search(arr, target) :
    lo = 0
    hi = len(arr)-1 
    
    # 일관성을 지키는 예외 처리 case 따라 택 1
    # 1. lower_bound
    if target > arr[-1] : return len(arr)
    # 2. upper_bound
    if target > arr[-1] : return len(arr)
    
    # 이진 탐색
    while lo < hi :
        mid = (lo + hi) // 2
        if arr[mid] < target : 
            lo = mid + 1
        elif arr[mid] > target :
            hi = mid
        else :
            # case 에 따라 아래 2가지 중 택 1
            
            # 1. lower_bound
            # hi = mid
            
            # 2. upper_bound
            lo = mid + 1 
    return lo

binary_search(arr, target)