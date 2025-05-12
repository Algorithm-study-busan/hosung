n = int(input())

MAX = 1_000_000
dp = [False] * (MAX+1)

for i in range(1, MAX+1) :
    s = str(i)
    ck = False
    for l in range(1, len(s)) :
        if ck : break
        for j in range(len(s)-l+1) :
            nn = int(s[j:j+l])
            if nn <= 0 : continue
            if dp[i-nn] == False : 
                dp[i] = True
                ck = True
                break

        
if dp[n] : 
    s = str(n)
    arr = []
    for l in range(1, len(s)) :
        for j in range(len(s)-l+1) :
            nn = int(s[j:j+l])
            if nn <= 0 : continue
            if dp[n-nn] == False :
                arr.append(nn)
    print(min(arr))
else : 
    print(-1)