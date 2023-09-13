def is_same_gradient(a,b,c,d, x,y) :
    return (y-b) / (x-a) == (y-d) / (x-a)

def solution(m, n, a, b, balls):
    ans_arr = []
    for (c, d) in balls :
        ans = 987654321
        tmp =  [(a+c)**2+(b-d)**2,
                (a-c)**2+(b+d)**2,
                (2*m-a-c)**2+(b-d)**2,
                (a-c)**2+(2*n-b-d)**2]
        
        if a == c :
            if b > d :
                ans = min(tmp[0], tmp[2], tmp[3])
            else :
                ans = min(tmp[0], tmp[1], tmp[2])
        elif b == d :
            if a > c :
                ans = min(tmp[1], tmp[2], tmp[3])
            else :
                ans = min(tmp[0], tmp[1], tmp[3])

        else :
            ans = min(tmp)
            if a < c and b < d :
                if is_same_gradient(a,b,c,d, 0, 0) :
                    ans = min(ans, (a+b)**2, (c+d)**2)
                    print(ans) 
            elif a > c and b < d :
                if is_same_gradient(a,b,c,d, m, 0) :
                    ans = min(ans, (2*n-a-c)**2 + (b+d)**2)
                    print(ans) 
            elif a > c and b > d :
                if is_same_gradient(a,b,c,d, m,n) :
                    ans = min(ans, (2*m-c-a)**2+(2*n-b-d)**2)
                    print(ans) 
            elif a < c and b > d :
                if is_same_gradient(a,b,c,d,0,n) :
                    ans = min(ans, (a+c)**2+(2*n-b-d)**2)
                    print(ans) 
                
        ans_arr.append(ans)
        print()
        
    return ans_arr
                
            

