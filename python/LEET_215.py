import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums :
            heapq.heappush(pq, -n)
        
        while k > 1:
            heapq.heappop(pq)
            k -= 1
        
        return -pq[0]
