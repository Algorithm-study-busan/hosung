import sys
sys.setrecursionlimit(10000000)

def solution(money):
    dp1 = [-1 for _ in range(len(money))]
    dp2 = [-1 for _ in range(len(money))]
    
    arr1 = money
    arr2 = [x for x in money[1:]]
    
    def find_dp(idx, arr, dp) :
        if idx < 0 : return 0
        if dp[idx] != -1 : return dp[idx]
    
        dp[idx] = max(arr[idx] + find_dp(idx-2, arr, dp), find_dp(idx-1, arr, dp))
        return dp[idx]
    
    return max(find_dp(len(arr1)-2, arr1, dp1), find_dp(len(arr2)-1, arr2, dp2))
        