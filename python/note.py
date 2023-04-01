n, m = map(int, input().split())
series = list(map(int, input().split()))
series = list(set(series))
series.sort()

result = []
def f(idx):
  if len(result) == m:
    print(*result)
    return
  
  for i in range(idx, len(series)):
    result.append(series[i])
    f(i)
    result.pop()

f(0)