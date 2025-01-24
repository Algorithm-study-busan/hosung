import sys

N = int(input())

arr = list(map(int,input().split()))

arr.sort()

print(arr[-1] + len(arr)-1)
    