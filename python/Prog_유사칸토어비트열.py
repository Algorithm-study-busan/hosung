def recur(l, r, s, e, k) :
    if s <= l and r <= e : return 4**k
    if e < l or s > r : return 0
    
    ret = 0
    for i in range(5) :
        if i == 2 : continue
        ret += recur(l + 5**(k-1)*i, l + 5**(k-1)*(i+1)-1, s, e, k-1)
    return ret

def solution(n, s, e):
    return recur(1, 5**n, s, e, n)
