def solution(friends, gifts):
    N = len(friends)
    mapping = dict()
    cnt = [[0 for _ in range(N)] for _ in range(N)]
    score = [0 for _ in range(N)]
    
    for i, name in enumerate(friends) :
        mapping[name] = i
        
    for gift in gifts :
        n1, n2 = gift.split()
        a,b = mapping[n1], mapping[n2]
        
        cnt[a][b] += 1
        score[a] += 1
        score[b] -= 1
    
    result = [0 for _ in range(N)]
    for a in range(N) :
        for b in range(a, N) :
            if cnt[a][b] == cnt[b][a] :
                if score[a] > score[b] : result[a] += 1
                elif score[a] < score[b] : result[b] += 1
            elif cnt[a][b] > cnt[b][a] :
                result[a] += 1
            else :
                result[b] += 1
        
    return max(result)