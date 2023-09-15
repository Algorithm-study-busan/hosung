def solution(R, C, x, y, queries):
    sr = x
    er = x
    sc = y
    ec = y
    
    for q in queries[::-1] :
        if not (0<=sr<R and 0<=er<R and 0<=sc<C and 0<=ec<C) : return 0
        
        if q[0] == 0 :
            ec = min(C-1, ec+q[1])
            if sc != 0 : sc += q[1]
        elif q[0] == 1 :
            sc = max(0, sc-q[1])
            if ec != C-1 : ec -= q[1]
        elif q[0] == 2 :
            er = min(R-1, er+q[1])
            if sr!= 0 : sr += q[1]
        elif q[0] == 3 :
            sr = max(0, sr-q[1])
            if er != R-1 : er -= q[1]
    
    return (er-sr+1) * (ec-sc+1)
        