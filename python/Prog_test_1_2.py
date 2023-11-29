from itertools import permutations

def solution(ability):
    n = len(ability[0])
    ans = 0
    for arr in permutations([x for x in range(10)]) :
        temp = 0
        for i in range(n) :
            temp += ability[arr[i]][i]
        ans = max(ans, temp)
    return ans

for arr in permutations([0,1,2,3]) :
    print(arr)