class Node :
    def __init__(self, n) :
        self.n = str(n)
    def __lt__(self, other) :
        s1 = self.n
        s2 = other.n
        
        return int(s1 + s2) > int(s2 + s1)

def solution(numbers):
    arr = sorted(map(Node, numbers))
    ans = ""
    for a in arr :
        ans += a.n
    
    if ans[0] == '0' : return "0"
    else : return ans
    