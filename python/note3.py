def print_sq(a, p) :
    SET = set()
    for e in range(p) :
        print(a ** e % p, end = " ")
        SET.add(a ** e % p)
    print()
    print(SET, len(SET))
    
def fact(n) :
    ret = 1
    for n in range(1, n+1) :
        ret *= n
    return ret

def gcd(a, b) :
    if b == 0 : return a
    return gcd(b, a%b)

def euler(n) :
    ret = 0
    for a in range(1, n) :
        if gcd(a, n) == 1 :
            ret += 1
    return ret

# print(euler(fact(10)))
# print(2**11 * 3**4 * 5)
# print(2**8 * 3**4 * 5**2 * 7)
# print(fact(10), 2**8 * 3**4 * 5**2 * 7)

a = 2 * 3 * 5
b = 2**4 * 3**2 * 5**2

print(euler(a), euler(b))
print(euler(a)/a, euler(b)/b)



    
