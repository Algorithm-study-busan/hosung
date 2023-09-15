def solution(topping):
    accumulate_set = []
    accumulate_set_reverse = []
    
    s = set()
    
    for t in topping :
        s.add(t)
        accumulate_set.append(len(s))
        
    s.clear()
    for t in topping[::-1] :
        s.add(t)
        accumulate_set_reverse.append(len(s))
        
    ans = 0
    for i in range(len(topping) - 1) :
        if accumulate_set[i] == accumulate_set_reverse[len(topping) -i -2] :
            ans += 1
            
    return ans
    
    