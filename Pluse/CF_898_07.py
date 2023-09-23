from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T) :
    s = input().strip()
    ans = s.count('A')
    if s[0] == 'A' and s[-1] == 'A' :
        if s.count('BB') != 0 : print(ans)
        else :
            arr = s.split('B')
            min_value = ans
            for a in arr :
                if len(a) == 0 : continue
                min_value = min(min_value, len(a))
            print(ans - min_value)
    else :
        print(ans)
    
