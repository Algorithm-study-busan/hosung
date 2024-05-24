
class Solution:
    def __init__(self) :
        self.dp = [-1 for _ in range(301)]
    
    def find_dp(self, idx, s, words) :
        if idx == len(s) : return 1
        if self.dp[idx] != -1 : return self.dp[idx]
        self.dp[idx] = 0
        for i in range(idx, len(s)) :
            if s[idx:i+1] in words :
                self.dp[idx] += self.find_dp(i+1, s, words)
        return self.dp[idx]

        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.find_dp(0, s, wordDict) > 0