def solution(k, ranges):
    arr = [k]
    
    while k != 1 :
        if k % 2 == 0 :
            k //= 2
        else :
            k = 3*k + 1
        arr.append(k)
        
    area = []
    for i in range(1, len(arr)) :
        area.append((arr[i] + arr[i-1])/2)
    
    area_sum = 0    
    accumulated_area = [0]
    for a in area :
        area_sum += a
        accumulated_area.append(area_sum)
        
    print(accumulated_area)
    
    # return answer

solution(5, [])