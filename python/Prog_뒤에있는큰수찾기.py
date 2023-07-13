def solution(numbers):
    q = []
    ans = []
    for n in numbers[::-1] :
        while q and q[-1] <= n :
            q.pop()
        if len(q) == 0 :
            ans.append(-1)
        else :
            ans.append(q[-1])
        q.append(n)
    return ans[::-1]
              