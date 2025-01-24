import sys
from collections import defaultdict

N, M = map(int, input().split())
freq = defaultdict(int)

for _ in range(N):
    s = input().strip()
    mask = 0
    for i, ch in enumerate(s):
        if ch == '1':
            mask |= (1 << i)
    freq[mask] += 1

distinct_masks = sorted(freq.keys())

answer = 0

for i, A in enumerate(distinct_masks):
    fA = freq[A]
    answer += fA * (fA - 1) // 2

    neighbors = []
    for bit1 in range(M):
        neighbors.append(A ^ (1 << bit1))
    for bit1 in range(M):
        for bit2 in range(bit1+1, M):
            neighbors.append(A ^ (1 << bit1) ^ (1 << bit2))

    for B in neighbors:
        if B > A and B in freq:
            answer += fA * freq[B]

print(answer)