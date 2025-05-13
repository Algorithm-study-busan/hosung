N = int(input())

edges = []
for n in range(1, N + 1):
    d = int(input())
    edges.append([0, n, d])

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for a in range(N) :
    for b in range(a+1, N) :
        edges.append([a+1, b+1, arr[a][b]])


node_set = [i for i in range(N+1)]

def find_parent(n) :
    if n == node_set[n] : return n
    node_set[n] = find_parent(node_set[n])
    return node_set[n]

def is_set(a,b) :
    a = find_parent(a)
    b = find_parent(b)
    return  a == b

def union_set(a,b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b : node_set[b] = a
    else : node_set[a] = b

edges.sort(key = lambda x : x[2])

ans = 0

for a,b,d in edges :
    if is_set(a,b) : continue
    union_set(a,b)
    ans += d

print(ans)
