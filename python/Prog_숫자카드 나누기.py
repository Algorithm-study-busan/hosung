def gcd(a, b) :
    c = a % b
    while c != 0 :
        a = b
        b = c
        c = a % b
    return b

def solution(arrayA, arrayB):
    answer = 0
    return answer

print(gcd(16, 30))