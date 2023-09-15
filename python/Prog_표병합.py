parent = [[]]
value = [[]]
R = 51
C = 51

def get_parent(r, c) :
    global parent, value
    if [r,c] == parent[r][c] :
        return [r,c]
    parent[r][c] = get_parent(*parent[r][c])
    return parent[r][c]

def update1(r,c, v) :
    global parent, value
    p = get_parent(r,c) 
    value[p[0]][p[1]] = v
    
def update2(v1, v2) :
    global parent, value
    for r in range(R) :
        for c in range(C) :
            if value[r][c] == v1 :
                value[r][c] = v2
                
def merge(r1, c1, r2, c2) :
    global parent, value
    p1 = get_parent(r1, c1)
    p2 = get_parent(r2, c2)
    
    if value[p1[0]][p1[1]] == "" :
        parent[p1[0]][p1[1]] = p2
    else :
        parent[p2[0]][p2[1]] = p1
        
def parent_match() :
    for r in range(R) :
        for c in range(C) :
            get_parent(r,c)
        
def unmerge(r, c) :
    global parent, value
    p = get_parent(r, c)
    tmp = value[p[0]][p[1]]
    
    parent_match()
    
    for ri in range(R) :
        for ci in range(C) :
            pi = get_parent(ri, ci)
            if pi == p :
                parent[ri][ci] = [ri, ci]
                value[ri][ci] = ""
                
    value[r][c] = tmp
    


def solution(commands):
    global parent, value
    parent = [[ [0,0] for _ in range(C)] for _ in range(R)]
    value = [["" for _ in range(C)] for _ in range(R)]
    
    for r in range(R) :
        for c in range(C) :
            parent[r][c] = [r,c]
            
    ans = []
            
    for command in commands :
        com = command.split()
        if com[0] == "UPDATE" :
            if len(com) == 4 :
                r,c = map(int, com[1:3])
                update1(r,c, com[3])
            else :
                v1,v2 = com[1:]
                update2(v1,v2)
        elif com[0] == "MERGE" :
            r1,c1,r2,c2 = map(int, com[1:])
            merge(r1,c1,r2,c2)
        elif com[0] == "UNMERGE" :
            r,c = map(int, com[1:])
            unmerge(r,c)
        else :
            r,c = map(int, com[1:])
            p = get_parent(r,c)
            x = value[p[0]][p[1]]
            ans.append("EMPTY" if x == "" else x)
    
    return ans
    
arr = []

def f() :
    global arr
    arr.append(2)
    h()
    
def h() :
    arr.append(3)