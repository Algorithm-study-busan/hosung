dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

ans = 0
words = []

def binary_search(x) :
    lo = 0
    hi = len(words)-1
    while lo < hi :
        mid = (lo + hi)//2
        if x <= words[mid] :
            hi = mid-1
        else :
            lo = mid+1
    return words[lo] == x

def dfs(i, tmp) :
    if i == 25 : 
        

with open("dict.txt", 'r') as f : 
    content = f.read() 
    words = content.split('\n')
    
    