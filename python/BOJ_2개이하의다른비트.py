def cal(b) :
    ret = int(b, 2)
    for i in range(len(b)) :
        if b[len(b)-1-i] == '0' :
            ret += 2**i
            for j in range(i, -1, -1) :
                if b[len(b)-1-j] == '1' :
                    ret -= 2**j
                    return ret
            return ret
    return ret - 2**(len(b)-1) + 2**len(b)
                    
        
def solution(numbers):
    ans = []
    for num in numbers : 
        ans.append(cal(bin(num)[2:]))
    return ans

print(solution([6]))