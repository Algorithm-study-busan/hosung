class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i, c in enumerate(citations, 1) :
            if i > c : break
            ans = i
        return ans
        