def to_int(time) :
    a,b = time.split(":")
    return int(a) * 60  + int(b)

def solution(plans):
    works = []
    for plan in plans : 
        works.append([plan[0], to_int(plan[1]), int(plan[2])])
        
    works.sort(key = lambda x : x[1])
    
    on_works = []
    ans = []
    
    for work in works :
        if not on_works : 
            on_works.append(work)
        else : 
            remain_time = work[1] - on_works[-1][1]
            
            while on_works and remain_time > 0 : 
                work_time = min(on_works[-1][2], remain_time)
                on_works[-1][2] -= work_time
                remain_time -= work_time
                
                if on_works[-1][2] == 0 :
                    ans.append(on_works.pop()[0])
            on_works.append(work)
            
    while on_works :
        ans.append(on_works.pop()[0])
    
    return ans
    
    
    
    
    