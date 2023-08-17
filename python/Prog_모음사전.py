from functools import cmp_to_key
from itertools import combinations

c = ['A', 'E', 'I', 'O', 'U']

def cmp(a, b) :
    for i in range(min(len(a), len(b))) :
        if a[i] < b[i] : return -1
        elif a[i] > b[i] : return 1
    
    return len(a) - len(b)

def find_arr(arr : list, s : list,l : int) :
    if len(s) == l : 
        arr.append(''.join(s))
        return
    for i in range(5) :
        s.append(c[i])
        find_arr(arr, s, l)
        s.pop(-1)

def solution(word):
    
    arr = []
    
    for l in range(1, 6) :
        find_arr(arr, [], l)
    
    arr.sort(key = cmp_to_key(cmp))
    print(arr[:10])
    
    for i, x in enumerate(arr, 1) :
        if word == x : return i

solution('A')
    