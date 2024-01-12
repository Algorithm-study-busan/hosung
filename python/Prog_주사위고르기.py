from itertools import combinations

def brute_x(x, idx, total, x_arr) :
    if idx == len(x) :
        x_arr.append(total)
        return

    for a in x[idx] :
        total += a
        brute_x(x, idx+1, total, x_arr)
        total -= a
        
def binary_search(x, arr) :
    lo = 0
    hi = len(arr)-1
    
    while lo <= hi :
        mid = (lo + hi)//2
        if arr[mid] <= x : lo = mid+1
        else : hi = mid-1
    return len(arr) - lo

def brute_y(y, idx, total, x_arr, res) :
    if idx == len(y) :
        res[0] += binary_search(total, x_arr)
        return
    for a in y[idx] :
        total += a
        brute_y(y, idx+1, total, x_arr, res)
        total -= a
    

def solution(dice):
    arr = [i for i in range(len(dice))]
    
    ans = []
    for comb in combinations(arr, len(dice)//2) :
        x = []
        y = []
        
        for i in range(len(dice)) :
            if i in comb : x.append(dice[i])
            else : y.append(dice[i])
        
        x_arr = []
        brute_x(x, 0, 0, x_arr)
        x_arr.sort()
        
        res = [0]
        brute_y(y, 0, 0, x_arr, res)
        
        ans.append([res[0], [i + 1 for i in comb]])
        
    ans.sort(key = lambda x : x[0])
    return ans[-1][1]
        
        
                
        
