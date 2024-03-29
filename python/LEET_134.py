class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx = 0
        total_gas = 0
        total_cost = 0
    
        N = len(gas)
        for i in range (2*N) :
            total_gas += gas[i % N]
            total_cost += cost[i % N]
            if i == start_idx + N : return start_idx
            if total_gas - total_cost < 0 :
                total_gas = 0
                total_cost = 0
                start_idx = i + 1
        return -1