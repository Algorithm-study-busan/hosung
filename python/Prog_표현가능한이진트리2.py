def cal_len(n) :
    ret = 1 
    while n >= 2**(ret) :
        ret = ret*2+1
    return ret

def to_bin_tree(n) :
    l = cal_len(n)
    b = str(bin(n)[2:])
    return "0" * (l-len(b)) + b

def check(bin_tree, s,e) :
    print(s,e)
    if s == e : return True
    mid = (e+s)//2
    if bin_tree[mid] == '0' :
        for i in range(s,e+1) :
            if bin_tree[i] == '1' : return False
        return True
    return check(bin_tree, s, mid-1) and check(bin_tree, mid+1, e)
    

def solution(numbers):
    ans = []
    for n in numbers :
        bin_tree = to_bin_tree(n)
        print(bin_tree)
        if check(bin_tree, 0, len(bin_tree)-1) :
            ans.append(1)
        else :
            ans.append(0)
    return ans
        