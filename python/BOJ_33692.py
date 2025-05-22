a,b = map(int, input().split())

ans_a = a
ans_b = b

e = 0

while a or b :
    if a % 2 == b % 2 :
        if a % 2 == 0 and ans_a + 2 ** e <= ans_b :
            ans_a += 2 ** e
                
        if a % 2 == 1 and ans_b - 2 ** e >= ans_a :
            ans_b -= 2 ** e
            
    a //= 2
    b //= 2
    e += 1
    
print(ans_a, ans_b)