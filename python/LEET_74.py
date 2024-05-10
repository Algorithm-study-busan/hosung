class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0 
        hi = len(matrix)-1

        while lo<=hi :
            mid = (lo+hi)//2
            if matrix[mid][-1] < target :
                lo = mid+1
            elif matrix[mid][-1] > target :
                hi = mid-1
            else :
                return True

        target_idx = lo
        if target_idx == len(matrix) : return False
        
        lo = 0
        hi = len(matrix[target_idx])-1

        while lo<=hi :
            mid = (lo+hi)//2
            if matrix[target_idx][mid] < target :
                lo = mid+1
            elif matrix[target_idx][mid] > target :
                hi = mid-1
            else :
                return True
        return False
        