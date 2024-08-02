class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lowerBound(arr, target) :
            lo = 0
            hi = len(arr)-1
            while lo <= hi :
                mid = (lo + hi)//2
                if arr[mid] < target : lo = mid+1
                else : hi = mid-1
            return lo

        arr = []
        for num in nums : 
            idx = lowerBound(arr, num)
            if idx == len(arr) : arr.append(num)
            else : arr[idx] = num
        return len(arr)
        