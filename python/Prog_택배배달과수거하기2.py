def get_i(arr, idx) :
    while arr[idx] == 0 :
        idx -= 1

def go(arr, idx, cap) :
    while idx >= 0 and cap > 0 :
        removed = min(arr[idx], cap)
        arr[idx] -= removed
        cap -= removed
        get_i(arr, idx)

def solution(cap, n, deliveries, pickups):
    answer = -1
    return answer

x = 10
def f(a) :
    a -= 1
    print(a)
    
f(x)
print(x)