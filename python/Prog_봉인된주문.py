def solution(n, bans):
    def intToStr(nn) :
        ret = ""
        while nn > 0 :
            nn -= 1
            ret += chr(97 + nn % 26)
            nn //= 26
        
        return ret[::-1]
        
    bans.sort(key = lambda x : [len(x), x])
    
    def compare(s1,s2) :
        if len(s1) == len(s2) :
            return s1 <= s2
        return len(s1) < len(s2)
    
    ans = intToStr(n)
    
    for ban in bans :
        if compare(ban, ans) :
            n += 1
            ans = intToStr(n)
        else :
            break
            
    return ans
        
    
    
        