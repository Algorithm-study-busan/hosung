def solution(want, number, discount):
    cnt = dict()
    for i in range(len(want)) :
        cnt[want[i]] = number[i]
    
    ans = 0
    tmp = 0
    for i in range(10) :
        if cnt.get(discount[i]) is not None and cnt[discount[i]] > 0:
            tmp += 1
            cnt[discount[i]] -= 1
    
    if tmp == 10 :
        ans += 1
    print(tmp)
        
    for i in range(10, len(discount)) :
        if cnt.get(discount[i-10]) is not None  :
            tmp -= 1
            cnt[discount[i-10]] += 1
        if cnt.get(discount[i]) is not None  and cnt[discount[i]] > 0:
            tmp += 1
            cnt[discount[i]] -= 1
        if tmp == 10 :
            ans += 1
            
        print(tmp)
            
    return ans

