def solution(h1, m1, s1, h2, m2, s2):
    sx = 720 * s1
    mx = 720 * m1 + 12 * s1
    hx = 3600 * (h1 % 12) + 60 * m1 + s1
    
    start_s = h1 * 3600 + m1 * 60 + s1
    end_s = h2 * 3600 + m2 * 60 + s2
    
    ans = 0
    
    for s in range(start_s, end_s) : 
        nsx = sx + 720 
        nmx = mx + 12
        nhx = hx + 1

        if (sx <= mx and nmx < nsx) :       
            ans += 1
        if (sx <= hx and nhx < nsx) : 
            ans += 1        
        sx = nsx % 43200
        mx = nmx % 43200
        hx = nhx % 43200
    
    if s2 == m2 == 0 : ans += 1
    if start_s == 0 : ans -= 1
    if start_s <= 43200 < end_s : ans -= 1
    
    
    return ans
