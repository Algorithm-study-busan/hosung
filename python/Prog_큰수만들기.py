def solution(number, k):
    arr = []
    for n in number :
        while arr and k > 0 and n > arr[-1] :
            arr.pop()
            k -= 1
        arr.append(n)
    
    while k > 0 :
        arr.pop()
        k -= 1
    return ''.join(arr)