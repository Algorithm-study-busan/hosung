def is_ok(cnt : dict):
    for v in cnt.values() :
        if v != 0 : return False
    return True
    

def solution(want, number, discount):
    cnt = dict()
    for i in range(len(want)) :
        cnt[want[i]] = number[i]
    
    ans = 0
    for i in range(10) :
        if cnt.get(discount[i]) is not None:
            cnt[discount[i]] -= 1
    
    if is_ok(cnt) : ans += 1
        
    for i in range(10, len(discount)) :
        if cnt.get(discount[i-10]) is not None :
            cnt[discount[i-10]] += 1
        if cnt.get(discount[i]) is not None :
            cnt[discount[i]] -= 1
        
        if is_ok(cnt) : ans += 1
            
    return ans

