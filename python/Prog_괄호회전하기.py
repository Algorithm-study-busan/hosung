def is_ok(s) :
    # ()
    small = 0
    # []
    mid = 0
    # {}
    large = 0
    for c in s :
        if c == '(' :
            small += 1
        elif c == '[' :
            mid += 1
        elif c == '{' :
            large += 1
        elif c == ')' :
            small -= 1
        elif c == ']' :
            mid -= 1
        elif c == '}' :
            large -= 1
        
        if small < 0 or mid < 0 or large < 0 : return False
    
    return small == 0 and mid == 0 and large == 0

def solution(s):
    s = list(s)
    ans = 0
    for _ in range(len(s)) :
        print(s)
        if is_ok(s) : ans += 1
        x = s.pop(0)
        s.append(x)
        
        
    return ans

print(solution("[](){}"))