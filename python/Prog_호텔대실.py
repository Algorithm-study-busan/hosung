class Node : 
    t = 0
    start = 0
    def __init__(self, t, start) :
        self.t = t
        self.start = start
        
    def __lt__(self, other) :
        if self.t == other.t :
            return self.start < other.start
        return self.t < other.t
    
    def __repr__(self) :
        return f"{self.t} {self.start}"
    
def to_int(time) :
    h,m = time.split(":")
    return int(h)*60 + int(m)

def solution(book_time):
    node_arr = []
    for book in book_time :
        s = to_int(book[0])
        e = to_int(book[1]) + 10
        node_arr.append(Node(s, 1))
        node_arr.append(Node(e, 0))
        
    node_arr.sort()
    
    print(node_arr)
    
    ans = 0
    tmp = 0
    for node in node_arr :
        if node.start == 1 : 
            tmp += 1
        else :
            tmp -= 1
        ans = max(ans, tmp)
        
    return ans

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])