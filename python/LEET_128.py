from collections import defaultdict 

class Solution:
    def __init__(self) :
        self.nums_set = [i for i in range(100_001)]
        self.idx_map = dict()
        self.count = dict()

    def get_parent(self, n) :
        if n == self.nums_set[n] : return n
        self.nums_set[n] = self.get_parent(self.nums_set[n])
        return self.nums_set[n]

    def is_set(self, a, b) :
        a = self.get_parent(a)
        b = self.get_parent(b)
        return a == b

    def union(self, a, b) :
        a = self.get_parent(a) 
        b = self.get_parent(b) 
        if a < b :
            self.nums_set[b] = a
            self.count[a] += self.count[b]
        else :
            self.nums_set[a] = b
            self.count[b] += self.count[a]

    def longestConsecutive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums) :
            self.count[i] = 1
            self.idx_map[num] = i

        for i, num in enumerate(nums) :
            if num-1 in self.idx_map and not self.is_set(self.idx_map[num-1], self.idx_map[num]) :
                self.union(self.idx_map[num-1], self.idx_map[num])
            if num+1 in self.idx_map and not self.is_set(self.idx_map[num], self.idx_map[num+1]) :
                self.union(self.idx_map[num], self.idx_map[num+1])

        ans = 0

        for i in range(len(nums)) :
            ans = max(ans, self.count[self.get_parent(i)])
    
        return ans

            

    