def solution(cards):
    n = len(cards)
    group = [0 for _ in range(n+1)]
    
    for idx in range(1, n+1) :
        k = idx
        while group[k] == 0 :
            group[k] = idx
            k = cards[k-1]
            
    result = []
    
    for i in range(1, n+1) :
        x = 0
        for g in group :
            if i == g : x += 1
        result.append(x)
        
    result.sort(reverse=True)
    
    if len(result) < 2 :
        return 0
    return result[0] * result[1]

print(solution([8,6,3,7,2,5,1,4]))