from collections import defaultdict

N = int(input())

prior = defaultdict(int)

nums = []

not_zero = set()

for _ in range(N) : 
    s = input()
    nums.append(s)
    arr = list(s)
    not_zero.add(s[0])
    
    e = 1
    while arr :
        c = arr.pop()
        prior[c] += e
        e *= 10
        
arr = [[k,v] for k,v in prior.items()]
arr.sort(key = lambda x : -x[1])

if len(arr) == 10 :
    if arr[-1][0] in not_zero :
        idx = 9
        while arr[idx][0] in not_zero :
            idx -= 1
        arr.append(arr.pop(idx))

map_n = dict()

n = 9
for k,v in arr :
    map_n[k] = n
    n -= 1

    
def mapping(s, map_n) :
    arr = list(s)
    ret = 0
    e = 1
    while arr :
        ret += map_n[arr.pop()] * e
        e *= 10
    return ret

ans = 0
for num in nums :
    ans += mapping(num, map_n)
    
print(ans)