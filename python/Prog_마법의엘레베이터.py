from collections import defaultdict

dp = defaultdict(int)

def find_e(n) :
    for i in range(1, len(str(n))+1) :
        if n % 10**i != 0 :
            return (i, n % 10**i)

def find_dp(n) :
    global dp
    print(n)
    if dp[n] != 0 : return dp[n]
    if n == 0 : return 0
    if n == 10**(len(str(n))-1) : return 1
    
    e, ne = find_e(n)
    plus_n = n + 10**e - ne
    k_plus = (10**e - ne)// (10**(e-1))
    minus_n = n - ne
    k_minus = (ne) // (10**(e-1))
    dp[n] = min(find_dp(plus_n) + k_plus, find_dp(minus_n) + k_minus)
    return dp[n]
    

def solution(storey):
    return find_dp(storey)

solution(5)