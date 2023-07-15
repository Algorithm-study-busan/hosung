def solution(scores):
    p_arr = []
    inct = [True for _ in range(len(scores))]
    
    for i,p in enumerate(scores) :
        p_arr.append([p[0], p[1], i])
        
    p_arr.sort()
    
    max_score = -1
    i = len(scores)-1
    
    while i > 0 :
        if p_arr[i][1] < max_score :
            inct[p_arr[i][2]] = False
        tmp_max_score = max(max_score, p_arr[i][1])
                
        while i > 0 and p_arr[i][0] == p_arr[i-1][0] :
            i -= 1
            tmp_max_score = max(tmp_max_score, p_arr[i][1])
            if p_arr[i][1] < max_score :
                inct[p_arr[i][2]] = False
                
        max_score = tmp_max_score
        i -= 1
    
    p_inct_arr = []
    for p in p_arr :
        if inct[p[2]] :
            p_inct_arr.append(p)
            
    ranks = [0 for _ in range(len(scores))]
    p_inct_arr.sort(key = lambda x : -(x[0] + x[1]))
    
    for rank, p in enumerate(p_inct_arr,1) :
        ranks[p[2]] = rank        
        
    for i in range(1, len(p_inct_arr)) :
        if p_inct_arr[i][0] + p_inct_arr[i][1] == p_inct_arr[i-1][0] + p_inct_arr[i-1][1] :
            ranks[p_inct_arr[i][2]] = ranks[p_inct_arr[i-1][2]]
            
    return -1 if ranks[0] == 0 else ranks[0]
