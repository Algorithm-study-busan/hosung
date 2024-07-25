import heapq
from collections import defaultdict

class Node :
    def __init__(self, sum, i1, i2) :
        self.sum = sum
        self.i1 = i1
        self.i2 = i2

    def __lt__(self, other) :
        return self.sum < other.sum

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        ans = []
        visited = [defaultdict(bool) for _ in range(len(nums1))]
        
        heapq.heappush(pq, Node(nums1[0] + nums2[0], 0, 0))
        visited[0][0] = True

        while k :
            top = heapq.heappop(pq)
            ans.append([nums1[top.i1], nums2[top.i2]])
            if top.i1 + 1 < len(nums1) and not visited[top.i1+1][top.i2]:
                heapq.heappush(pq, Node(nums1[top.i1+1] + nums2[top.i2], top.i1+1, top.i2))
                visited[top.i1+1][top.i2] = True
            if top.i2 + 1 < len(nums2) and not visited[top.i1][top.i2+1] : 
                heapq.heappush(pq, Node(nums1[top.i1] + nums2[top.i2+1], top.i1, top.i2+1))
                visited[top.i1][top.i2+1] = True
            k -= 1

        return ans