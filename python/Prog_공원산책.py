move = {
    "N" : [-1,0],
    "S" : [1, 0],
    "W" : [0,-1],
    "E" : [0, 1]
}
R = 0
C = 0
park = []

def in_range(r,c) :
    return 0<=r<R and 0<=c<C

def can_go(r, c, d, k) :
    for _ in range(k) :
        r += move[d][0]
        c += move[d][1]
        
        if not in_range(r,c) or park[r][c] == 'X' : return False
    
    return True

def solution(park_, routes):
    global R, C, park
    park = park_
    R = len(park)
    C = len(park[0])
    
    sr = -1
    sc = -1
    for r in range(R) :
        for c in range(C) :
            if park[r][c] == "S" :
                sr = r
                sc = c
    
    for route in routes :
        d, k = route.split()
        k = int(k)
        if can_go(sr,sc, d,k) :
            sr += move[d][0] * k
            sc += move[d][1] * k
        
    return sr, sc
        
        
    
    
            