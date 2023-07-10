def solution(r1, r2):
    ans = 0
    for x in range(1, r2+1) :
        y = (r2**2 - x**2)**0.5
        limit = int(y)
        ans += limit+1
    
    for x in range(1, r1+1) :
        y = (r1**2 - x**2)**0.5
        limit = int(y)-1 if int(y) == (r1**2 - x**2)**0.5 else int(y)
        ans -= limit+1
        
    return ans*4

print(solution(2,3))
        
        