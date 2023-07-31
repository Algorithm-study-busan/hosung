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
        
    print(accumulate_set)
    print(accumulate_set_reverse)
    
solution([1, 2, 1, 3, 1, 4, 1, 2])
    
    