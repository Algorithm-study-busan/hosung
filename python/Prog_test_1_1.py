def mapping(c) :
    return ord(c) - ord('a')

def solution(input_string):
    check = [False for _ in range(26)]
    set_arr = set()
    for i, c in enumerate(input_string) :
        if i != 0 and c == input_string[i-1] : continue
        if check[mapping(c)] :
            set_arr.add(c)
        check[mapping(c)] = True
        
    set_arr = list(set_arr)
    if len(set_arr) == 0 : 
        return 'N'
    set_arr.sort()
    return ''.join(set_arr)
            
print(solution("eeddee"))