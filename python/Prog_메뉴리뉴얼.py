from itertools import combinations

contain = [[False for _ in range(26)] for _ in range(20)]

def is_contain(order : str, menu, idx) :
    for m in menu :
        if contain[idx][ord(m)-65] == 0 : return False
    return True

def count(orders, menu) :
    ret = 0
    for i, order in enumerate(orders) :
        if is_contain(order, menu, i) : ret += 1
    return ret
    

def solution(orders, course):
    global contain
    
    for i, order in enumerate(orders) :
        for o in order :
            contain[i][ord(o)-65] = True
    
    
    comb = set()
    for order in orders :
        for c in course :
            comb |= set(combinations(sorted(order), c))
                
    tmp = [[] for _ in range(11)]
    tmp_count = [0 for _ in range(11)]
            
    for menu in comb :
        cnt = count(orders, menu)
        
        if cnt >= 2 and tmp_count[len(menu)] < cnt :
            tmp[len(menu)] = [''.join(menu)]
            tmp_count[len(menu)] = cnt
        elif cnt >= 2 and tmp_count[len(menu)] == cnt :
            tmp[len(menu)].append(''.join(menu))
            
    ans = []
    for t in tmp :
        if t :
            for x in t :
                ans.append(x)
    
    ans.sort()
    return ans
