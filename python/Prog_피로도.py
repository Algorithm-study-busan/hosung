from itertools import permutations

def cal(k, order, dungeons) :
    ret = 0
    for i in order :
        if dungeons[i][0] > k : break
        ret += 1
        k -= dungeons[i][1]
    return ret

def solution(k, dungeons):
    ans = 0
    orders = permutations([i for i in range(len(dungeons))])
    for order in orders :
        ans = max(ans, cal(k, order, dungeons))
    return ans