def solution(words):
    words.sort()
    
    ans = 0
    
    def calSamePart(s1, s2) :
        cnt = 0
        for i in range(min(len(s1), len(s2))) :
            if s1[i] != s2[i] : return cnt
            cnt += 1
        return cnt
    
    for i in range(len(words)) :
        if i == 0 :
            ans += min(len(words[i]), calSamePart(words[i], words[i+1]) + 1)
        elif i == len(words) -1 :
            ans += min(len(words[i]), calSamePart(words[i], words[i-1]) + 1)
        else :
            ans += min(len(words[i]), max(calSamePart(words[i], words[i-1]), calSamePart(words[i], words[i+1]))+1)
        
    return ans
            