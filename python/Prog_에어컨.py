import sys
sys.setrecursionlimit(1_000_000)

MAX = 1000
INF = 987654321
dp = [[-1 for _ in range(MAX)] for _ in range(2051)]

temperature = 0
t1 = 0
t2 = 0
a = 0
b = 0
onBoard = []

def cal_t(t) :
    if t < temperature : return t + 1
    elif t > temperature : return t - 1
    return t

def find_dp(now_t, idx) :
    if idx == len(onBoard) : return 0
    if dp[now_t][idx] != -1 : return dp[now_t][idx]
    if onBoard[idx] and (now_t > t2 or now_t < t1) : return INF

    ret = min(a + find_dp(now_t-1, idx+1),
              b + find_dp(now_t, idx+1),
              a + find_dp(now_t+1, idx+1),
              find_dp(cal_t(now_t), idx+1))
    
    dp[now_t][idx] = ret
    return ret

def solution(temperature_, t1_, t2_, a_, b_, onboard_):
    global temperature, t1, t2, a, b, onBoard
    temperature = temperature_ + 1010
    t1 = t1_ + 1010
    t2 = t2_ + 1010
    a = a_ 
    b = b_  
    onBoard = onboard_
    
    return find_dp(temperature, 0)