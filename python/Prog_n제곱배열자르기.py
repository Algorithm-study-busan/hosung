N = 0

def cal_x(idx) :
    col = idx // N
    row = idx % N
    if row < col : return col+1
    return row+1

def solution(n, left, right):
    global N
    N = n
    ans = []
    for idx in range(left, right+1) :
        ans.append(cal_x(idx))
    return ans