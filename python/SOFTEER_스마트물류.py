import sys

N, K = map(int, input().split())

line = input()

selected = [False for _ in range(N)]

ans = 0
for i in range(len(line)) :
    if line[i] != 'P' : continue
    for j in range(max(0, i-K), min(N, i+K+1)) :
        if line[j] == 'H' and not selected[j] : 
            selected[j] = True
            ans += 1
            break

print(ans)