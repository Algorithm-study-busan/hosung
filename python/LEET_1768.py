class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        l = min(len(word1), len(word2))
        for i in range(l) :
            ans += word1[i]+word2[i]
        ans += word1[l:] + word2[l:]
        return ans
        