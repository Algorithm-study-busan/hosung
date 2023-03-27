N,M = map(int, input().split())
MOD = 1000

MT = []
for _ in range(N) :
    MT.append(list(map(int, input().split())))
    
for a in range(N) :
    for b in range(N) :
        MT[a][b] = MT[a][b] % MOD 
    
def mul_mt(m1, m2) :
    ret = [[0 for _ in range(N)] for _ in range(N)]
    for a in range(N) :
        for b in range(N) :
            x = 0
            for i in range(N) :
                x += m1[a][i] * m2[i][b]
            ret[a][b] = x % MOD
    return ret
    

def exp(mt, m) :
    if m == 1 : return mt
    sub_mt = exp(mt, m//2)
    if m % 2 == 1 :
        return mul_mt(mt, mul_mt(sub_mt, sub_mt))
    else :
        return mul_mt(sub_mt, sub_mt)
    
ans = exp(MT, M)

for a in ans :
    print(*a)
    