ans_arr = []
tmp_diff = 0
tmp_arr = [0 for _ in range(11)]
info = []

def dfs(idx, n, score_a, score_b) :
    global ans_arr, tmp_diff, tmp_arr
    if idx == 11 :
        diff = score_b-score_a
        if score_a < score_b and tmp_diff <= diff :
            ans = tmp_arr[::]
            if n > 0 : ans[10] = n
            
            if tmp_diff < diff : ans_arr.clear()
            ans_arr.append(ans)
            tmp_diff = score_b - score_a
        return
    
    if info[idx] > 0 : next_score_a = score_a + (10-idx)
    else : next_score_a = score_a
    dfs(idx+1, n, next_score_a, score_b)
    
    if n > info[idx] :
        tmp_arr[idx] = info[idx]+1
        dfs(idx+1, n-(info[idx]+1), score_a, score_b+(10-idx))
        tmp_arr[idx] = 0

    

def solution(n, info_):
    global info
    info = info_
    dfs(0, n, 0, 0) 
    ans_arr.sort(key = lambda x : x[::-1], reverse=True)
    if len(ans_arr) == 0 : return [-1]
    else : return ans_arr[0]
