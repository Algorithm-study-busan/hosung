import sys
sys.setrecursionlimit(10000000)

def solution(k, room_number):
    num_set = dict()
    
    def get_parent(n) :
        if n not in num_set : 
            num_set[n] = n
            return n
        
        if num_set[n] != n :
            num_set[n] = get_parent(num_set[n])
            return num_set[n]
        return n
    
    def union(a) :
        a = get_parent(a)
        b = get_parent(a+1)
        num_set[a] = b
        
    ans = []
    for num in room_number :
        ans.append(get_parent(num)) 
        union(num)
    return ans
            
            