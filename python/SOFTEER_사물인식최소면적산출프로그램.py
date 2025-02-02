import sys

N, K = map(int, input().split())

arr = []
for _ in range(N) :
    x,y, p = map(int, input().split())
    arr.append([x,y,p])

arr.sort(key = lambda x : x[1])

def find_y2(x1, x2, y1) :
    num = set()
    for x,y,p in arr :
        if x1 <= x <= x2 and  y >= y1 : 
            num.add(p)
            if len(num) == K : return y
    return -2000
            
ans = 987654321

for i in range(N) :
    for j in range(N) :
        for k in range(N) :
            x1 = min(arr[i][0], arr[j][0], arr[k][0])
            y1 = min(arr[i][1], arr[j][1], arr[k][1])
            x2 = max(arr[i][0], arr[j][0], arr[k][0])
            y2 = find_y2(x1, x2, y1)
            if y2 != -2000 : ans = min(ans, (x2-x1) * (y2-y1))
print(ans)
        
        
        