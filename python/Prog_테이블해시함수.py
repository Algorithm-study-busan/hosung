def cal_sum(arr, mod) :
    ret = 0
    for a in arr :
        ret += a % mod
    return ret
        

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col-1], -x[0]))
    
    ans = 0
    for i in range(row_begin, row_end+1) :
        ans ^= cal_sum(data[i-1], i)
    print(ans)
    return ans
        
        
        
    
solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)