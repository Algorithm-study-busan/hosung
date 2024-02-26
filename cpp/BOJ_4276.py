def count(n) :
    if n == -1 : return 0
    if n < 10 : return 1
    length = len(str(n))
    
    ret = int(str(n)[:length-1])+1
    
    for i in range(1, length-1) :
        if str(n)[length-1-i] == '0' :
            ret += (int(str(n)[:length-1-i])-1) * (10**i)
            ret += int(str(n)[length-i:])+1
        else :
            ret += (int(str(n)[:length-1-i])) * (10**i)
        
    return ret



while True :
    a,b = map(int ,input().split())
    if a < 0 : break
    print(count(b) - count(a-1))

        
        
        
        
