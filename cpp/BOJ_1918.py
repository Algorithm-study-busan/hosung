from collections import deque

s = input()
stck = deque()

for c in s :
    if 'A' <= c <= 'Z' :
        print(c, end='')
    elif c == '(' :
        stck.append(c)
    elif c == '-' or c == '+' :
        while stck and stck[-1] != '(' :
            print(stck.pop(), end='')
        stck.append(c)
    elif c == '*' or c == '/' :
        while stck and (stck[-1] == '*' or stck[-1] == '/') :
            print(stck.pop(), end='')
        stck.append(c)
    elif c == ')' :
        while stck and stck[-1] != '(' :
            print(stck.pop(), end='')
        stck.pop()
        
while stck :
    print(stck.pop(), end='')
            

