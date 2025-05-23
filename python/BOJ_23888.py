import sys
input = sys.stdin.readline

a,d = map(int, input().split())

M = int(input())

def gcd(a,b) :
    while b :
        c = a % b
        a,b = b,c
    return a

for _ in range(M) :
    k,l,r = map(int, input().split())
    if k == 1 :
        n = r-l+1
        al = a + d*(l-1)
        ar = a + d*(r-1)
        print(n * (al + ar) // 2)
    else :
        al = a + d*(l-1)
        if l == r : print(al)
        else : print(gcd(al, d))

