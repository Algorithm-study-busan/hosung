import sys
from itertools import combinations

arr = list(map(int, input().split()))

fight = list(combinations([0,1,2,3], 2))


ans = 0
def dfs(fight, idx, prob, score) :
    global ans
    if idx == len(fight) :
        cnt = 0
        for s in score :
            if s > score[0] : cnt += 1
        if cnt <= 1 : 
            ans += prob
        return

    i = fight[idx][0]
    j = fight[idx][1]
    win_prob = arr[i] * 4 / (5*arr[i] + 5*arr[j])
    lose_prob = arr[j] * 4 / (5*arr[i] + 5*arr[j])
    draw_prob = (arr[i] + arr[j]) / (5*arr[i] + 5*arr[j])

    score[i] += 3
    dfs(fight, idx+1, prob*win_prob, score)
    score[i] -= 3

    score[j] += 3
    dfs(fight, idx+1, prob*lose_prob, score)
    score[j] -= 3

    score[i] += 1
    score[j] += 1
    dfs(fight, idx+1, prob*draw_prob, score)
    score[i] -= 1
    score[j] -= 1

dfs(fight, 0, 1, [0,0,0,0])
print(f"{ans*100:.3f}")
    
    
    