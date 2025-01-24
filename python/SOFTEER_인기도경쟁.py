import sys

N = int(input())

X = 0
for _ in range(N) :
    pi, ci = map(int, input().split())
    if abs(pi - X) <= ci :
        X += 1
print(X)
    