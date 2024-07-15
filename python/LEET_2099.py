import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for idx, num in enumerate(nums) :
            if len(pq) < k : heapq.heappush(pq, [num, idx])
            else :
                if pq[0][0] < num : 
                    heapq.heappop(pq)
                    heapq.heappush(pq, [num, idx])

        pq.sort(key = lambda x : x[1])
        ans = []
        for num, idx in pq :
            ans.append(num)
        return ans
        