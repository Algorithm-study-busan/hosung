def cal_height(x, k) :
    return int((k**2 - x**2) ** 0.5)
    

def solution(k, d):
    ans = 0
    for x in range(0, d+1, k) :
        ans += cal_height(x, d)//k + 1
    return ans


print(solution(1, 5))
        