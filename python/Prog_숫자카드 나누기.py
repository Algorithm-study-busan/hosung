def gcd(a, b) :
    c = a % b
    while c != 0 :
        a = b
        b = c
        c = a % b
    return b

def cal_array_gcd(array) : 
    ret = array[0]
    
    for x in array :
        ret = gcd(ret, x)
        
    return ret

def solution(arrayA, arrayB):
    gcdA = cal_array_gcd(arrayA)
    gcdB = cal_array_gcd(arrayB)
    
    ansA = gcdA
    ansB = gcdB
    
    for b in arrayB :
        if b % gcdA == 0 : 
            ansA = 0
            break
        
    for a in arrayA :
        if a % gcdB == 0 :
            ansB = 0
            break
        
    return max(ansA, ansB)
