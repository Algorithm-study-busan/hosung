from itertools import combinations


def is_contain(order : str, menu) :
    for m in menu :
        if order.count(m) == 0 : return False
    return True

def count(orders, menu) :
    ret = 0
    for order in orders :
        if is_contain(order, menu) : ret += 1
    return ret
    

def solution(orders, course):
    alpha = set()
    for order in orders :
        for food in order :
            alpha.add(food)
            
    alpha = sorted(list(alpha))
    
    tmp = [[] for _ in range(11)]
    tmp_count = [0 for _ in range(11)]
            
    for c in course :
        for menu in combinations(alpha, c) :
            cnt = count(orders, menu)
            
            if cnt >= 2:
                print(''.join(menu, cnt))
            if cnt >= 2 and tmp_count[c] < cnt :
                tmp[c] = [[''.join(menu)]]
            elif cnt >= 2 and tmp_count[c] == cnt :
                tmp[c].append(''.join(menu))
            
    ans = []
    for t in tmp :
        if t :
            for x in t :
                ans.append(x)
    
    ans.sort()
    return ans
