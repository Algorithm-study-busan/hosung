def solution(arr, k):
    s = len(arr)-1
    e = len(arr)-1
    ans_a = 0
    ans_e = 0
    total = arr[s]
    min_len = 987654321
    
    while s > 0 and e > 0 :
        if total < k :
            s -= 1
            total += arr[s]
        elif total > k :
            e -= 1
            total -= arr[e]
        else :
            if min_len >= e-s+1 :
                min_len = e-s+1
                ans_s = s
                ans_e = e
            s -= 1
            total += arr[s]
            
    return [ans_s, ans_e]