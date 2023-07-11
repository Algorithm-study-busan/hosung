def mapping(mineral) :
    if mineral == "diamond" : return 0
    elif mineral == "iron" : return 1
    else : return 2

tired = [[1,1,1], [5,1,1], [25,5,1]]
ans = 987654321

def get_sum(gock, minerals, idx) :
    ret = 0
    for i in range(idx, min(len(minerals), idx+5)) :
        ret += tired[gock][minerals[i]]
    return ret

def brute_force(picks, minerals, idx, tmp) :
    global ans
    if sum(picks) == 0 or idx >= len(minerals) : 
        ans = min(ans, tmp)
        return
        
    for i in range(3) :
        if picks[i] == 0 : continue
        picks[i] -= 1
        brute_force(picks, minerals, idx+5, tmp + get_sum(i, minerals, idx))
        picks[i] += 1
        

def solution(picks, minerals):
    minerals = list(map(mapping, minerals))
    brute_force(picks, minerals, 0, 0)
    return ans