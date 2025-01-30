import sys

K, P, N = map(int, input().split())
MOD = 1_000_000_007

def find(p, n) :
    if n == 0 : return 1
    if n == 1 : return p

    tmp = find(p, n//2)
    
    if n % 2 == 0 :
        return (tmp * tmp) % MOD
    else :
        return (tmp * tmp * p) % MOD

print((K * find(P, N*10)) % MOD)
        