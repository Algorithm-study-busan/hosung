def find_ans(s, cnt) :
    for i in range(len(s)) :
        if s[i:i+3] == "111" :
            return s[:i] + "110"*cnt + s[i:]
    if s[-2:] == "11" :
        return s[:-2] + "110"*cnt + "11"
    elif s[-1:] == "1" :
        return s[:-1] + "110"*cnt + '1'
    return s + "110"*cnt

def solution(ss):
    ans = []
    for s in ss :
        cnt = 0
        one = 0
        s_removed = []
        for c in s:
            if c == '1' : 
                one += 1
                s_removed.append(c)
            else :
                if one < 2 : 
                    one = 0
                    s_removed.append(c) 
                else :
                    one -= 2
                    s_removed.pop()
                    s_removed.pop()
                    cnt += 1
        
        print(s_removed, cnt)
        ans.append(find_ans("".join(s_removed), cnt))
    return ans


print(solution(["100111100"]))