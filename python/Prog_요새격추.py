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
    
arr = []
arr.append(Roket(3, False, 1))
arr.append(Roket(2, True, 1))
arr.append(Roket(1, False, 1))
arr.append(Roket(2, False, 1))

arr.sort()

for roket in arr :
    print(roket.x, roket.start)
        
        