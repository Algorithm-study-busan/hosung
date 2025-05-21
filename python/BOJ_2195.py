S = input()
P = input()

word = set()
for i in range(len(S)) :
    for j in range(i+1, len(S)+1) :
        word.add(S[i:j])

ans = 0

l = 0
r = 1
while r <= len(P) :
    if P[l:r] in word :
        r += 1
    else :
        ans += 1
        l = r-1

print(ans+1)
