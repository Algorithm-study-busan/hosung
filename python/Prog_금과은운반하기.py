a = 0 
b = 0
g = []
s = []
w = []
t = []

def check(x) :
    max_g = 0
    max_s = 0
    can_move = 0
    
    for i in range(len(g)) :
        cnt = 0
        if t[i] <= x : cnt += 1
        cnt += (x-t[i]) // (2*t[i])
        
        max_g += min(g[i], cnt*w[i])
        max_s += min(s[i], cnt*w[i])
        can_move += min(g[i]+s[i], cnt*w[i])
    
    if max_g >= a and max_s >= b and can_move >= a+b :
        return True
    return False
        
    

def binary_search() :
    lo = 1
    hi = int(1e15)
    
    while lo <= hi :
        mid = (lo+hi) // 2
        if check(mid) : hi = mid-1
        else : lo = mid+1
    
    return lo

def solution(a_, b_, g_, s_, w_, t_):
    global a,b,g,s,w,t
    a = a_
    b=b_
    g=g_
    s=s_
    w=w_
    t=t_
    return binary_search()

# print(solution(10,10, [100], [100], [7], [10]))