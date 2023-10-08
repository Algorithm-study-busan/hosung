from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T) :
    n,m,k,H = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for a in arr :
        if abs(a-H) % k != 0 or abs(a-H) // k >= m : continue
        print(a)
        ans += 1
    print(ans)