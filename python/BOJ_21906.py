s = input()

last_idx = len(s)-1

cnt = 0
for i in range(len(s)-1, -1, -1) :
    if s[i] == '1' : 
        cnt += last_idx - i
        last_idx -= 1

print("Alice" if cnt % 3 != 0 else "Bob")
