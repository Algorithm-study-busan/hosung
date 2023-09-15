def cal(n) :
    if n < 10 :
        return min(n, 11-n)
    
    m = n%10
    return min(m + cal(n//10), 10-m + cal(n//10+1))

def solution(storey):
    return cal(storey)