def to_k(n, k) :
    ret = ""
    while n :
        ret += str(n % k)
        n //= k
    return ret[::-1]

def is_prime(n) :
    if n == 1 : return False
    for d in range(2, int(n**0.5)+1) :
        if n % d == 0 : return False
    return True

def solution(n, k):
    kn = to_k(n, k)
    arr = kn.split("0")
    
    ans = 0
    for n in arr :
        if n == "" : continue

        if is_prime(int(n)) : ans += 1
    return ans



