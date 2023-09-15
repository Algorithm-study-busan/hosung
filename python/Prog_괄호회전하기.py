def is_ok(s) :
    q = []
    pair = {')' : '(', ']' : '[', '}' : '{'}
    for c in s :
        if c == '(' or c == '[' or c == '{':
            q.append(c)
        else :
            if len(q) != 0 and q[-1] == pair[c] :
                q.pop()
            else :
                return False
    
    return len(q) == 0

def solution(s):
    s = list(s)
    ans = 0
    for _ in range(len(s)) :
        
        if is_ok(s) : ans += 1
        x = s.pop(0)
        s.append(x)
        
        
    return ans

print(solution("[](){}"))

"{[}]"