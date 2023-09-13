class Roket :
    x = 0
    start = 0
    n = 0
    def __init__(self, x, start, n) :
        self.x = x
        self.start = start
        self.n = n
        
    def __lt__(self, other) :
        if self.x == other.x :
            return self.start < other.start
        return self.x < other.x
    
def solution(targets):
    roket_arr = []
    for i, target in enumerate(targets) :
        roket_arr.append(Roket(target[0], True, i))
        roket_arr.append(Roket(target[1], False, i))
        
    roket_arr.sort()
    
    distroied = [False for _ in range(len(targets))]
    on_target = []
    
    ans = 0
    
    for i,roket in enumerate(roket_arr) :
        if distroied[roket.n] or (i > 0 and roket.x == roket_arr[i-1] and roket.start == False and roket_arr[i-1] == False): continue
        if roket.start :
            on_target.append(roket.n)
        else :
            ans += 1
            while on_target :
                distroied[on_target.pop()] = True
            
    return ans
        
        
        