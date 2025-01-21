from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = deque([])

        start = 0
        ans = 0
        for i,n in enumerate(nums) :
            if n == 0 : 
                if k > 0 :
                    k -= 1
                    zero.append(i)
                else :
                    if zero :
                        start = zero.popleft()+1
                        zero.append(i)
                    else :
                        start = i+1

            ans = max(ans, i-start+1)

        return ans 
                
        