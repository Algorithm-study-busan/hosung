N,K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

diff = []
for i in range(1, len(arr)) :
    diff.append(arr[i] - arr[i-1])
    
diff.sort(reverse = True)

print(sum(diff[K-1:]))