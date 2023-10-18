from collections import defaultdict

def is_all_same(arr) :
    fx = arr[0]
    for a in arr :
        if fx != a : return False
    return True

def solution(arr):
    if len(arr) == 1 : return 0
    if is_all_same(arr) : return 0
    
    last_idx = [-10 for _ in range(len(arr))]
    check = [False for _ in range(len(arr))]
    cnt = defaultdict(int)
    for i,a in enumerate(arr) :
        if i == 0 : 
            check[a] = True
            cnt[a] += 1
        elif last_idx[a] == i-1 : 
            if not check[a] :
                cnt[a] += 1
        elif check[a] and i - last_idx[a] > 2 :
            check[a] = False
            cnt[a] += 1
        else :
            cnt[a] += 1
        last_idx[a] = i

    print(cnt)
    max_cnt = 0
    for k, v in cnt.items() :
        max_cnt = max(max_cnt, v)
    return max_cnt*2

print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))