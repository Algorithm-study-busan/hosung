import sys
from itertools import permutations

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))

ans = 987654321

def find_tmp(line) :
    idx = 0
    tmp = 0
    for _ in range(K) :
        total = 0
        while total + line[idx] <= M :
            total += line[idx]
            idx += 1
            idx %= N
        tmp += total
    return tmp

for line in permutations(arr) :
    ans = min(ans, find_tmp(line))

print(ans)
    