dp = [set() for _ in range(9)]

def mapN(N, k) :
    return int(str(N) * k)

def already_in(n, k) :
    for i in range(1, k) :
        if n in dp[i] : return True
    return False

def solution(N, number):
    for k in range(1, 9) :
        dp[k].add(mapN(N, k))
    
    for k in range(2, 9) :
        for i in range(1, k) :
            for n1 in dp[i] :
                for n2 in dp[k-i] :
                    if not already_in(n1 + n2, k) : dp[k].add(n1 + n2)
                    if not already_in(n1 - n2, k) : dp[k].add(n1 - n2)
                    if not already_in(n1 * n2, k) : dp[k].add(n1 * n2)
                    if n2 != 0 and not already_in(n1 // n2, k) : dp[k].add(n1 // n2)
    
    for k in range(1, 9) :
        if number in dp[k] : return k
    return -1
    