from collections import defaultdict

def solution(clothes):
    clo = defaultdict(int)
    
    for a, b in clothes :
        clo[b]+=1
        
    ans = 1
    for k,v in clo.items() :
        ans *= (v+1)
        
    ans -= 1
    
    return ans