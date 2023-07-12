INF = 987654321

def solution(sequence):
    s1 = []
    s2 = []
    k = [-1,1]
    for i, x in enumerate(sequence) : 
        s1.append(x * k[i%2])
        s2.append(x * k[(i+1)%2])
        
    total1 = -INF
    total2 = -INF
    ans = -INF
    
    for i in range(len(sequence)) :
        total1 += s1[i]
        if s1[i] > total1 :
            total1 = s1[i]
        
        total2 += s2[i]
        if s2[i] > total2 :
            total2 = s2[i]
        
        ans = max(ans, total1, total2)
        
            
    return ans