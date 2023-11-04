def compare(date1, date2) :
    y1,m1,d1 = map(int, date1.split("."))
    y2,m2,d2 = map(int, date2.split("."))
    if y1 > y2 : return True
    elif y1 < y2 : return False
    else :
        if m1 > m2 : return True
        elif m1 < m2 : return False
        else :
            if d1 > d2 : return True
            else : return False
            
def plus(date, M) :
    y,m,d = map(int, date.split("."))
    m += M
    
    if m > 12 :
        y += (m-1) // 12
        m = (m-1) % 12 + 1
    d -= 1
    if d == 0 :
        d = 28
        m -= 1
        if m == 0 :
            m = 12
            y -= 1
    return f"{y}.{m:0>2}.{d:0>2}"
    
print(plus("2020.01.02", 2))