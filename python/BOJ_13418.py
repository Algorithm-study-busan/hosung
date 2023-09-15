from sys import stdin
input = stdin.readline

edges = []
V,E = map(int, input().split())
SET = [i for i in range(V+1)]

def get_parent(a) :
    if a == SET[a] : return a
    SET[a] = get_parent(SET[a])
    return SET[a]

def is_set(a, b) :
    a = get_parent(a)
    b = get_parent(b)
    return a == b

def union_node(a,b) :
    a = get_parent(a)
    b = get_parent(b)
    if a < b : SET[b] = a
    else : SET[a] = b
    
def MST() :
    ret = 0
    for a,b,c in edges :
        if is_set(a,b) : continue
        union_node(a,b)
        ret += (c == 0)
    return ret**2

for _ in range(E+1) :
    edges.append(list(map(int, input().split())))
    
edges.sort(key = lambda x : x[2])
max_cost = MST()

edges.sort(key = lambda x : -x[2])
SET = [i for i in range(V+1)]
min_cost = MST()

print(max_cost - min_cost)