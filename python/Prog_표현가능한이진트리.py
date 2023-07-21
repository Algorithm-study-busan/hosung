import math

ans = 1

def get_length(n) :
    n = int(math.log2(n) + 1)
    x = 1
    while x <= n :
        x *= 2
    return x-1

def binary_search(l, r, is_zero_parent, s) :
    global ans
    mid = (l+r)//2
    if s[mid] == '1' and is_zero_parent :
        ans = 0
        return
    if l == r : return
    is_zero_parent = is_zero_parent or s[mid] == '0'
    binary_search(l, mid-1, is_zero_parent, s)
    binary_search(mid+1, r, is_zero_parent, s)

def solution(numbers):
    global ans
    str_bin = []
    for n in numbers :
        l = get_length(n)
        str_bin.append(f"{bin(n)[2:]:0>{l}}")
    
    ans_arr = []
    
    print(*str_bin)
    
    for s in str_bin :
        ans = 1
        binary_search(0, len(s)-1, False, s)
        ans_arr.append(ans)
    
    return ans_arr
    
print(solution([7, 42, 5]))
