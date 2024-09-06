def solution(cookie):
    
    ans = 0
    for mid in range(len(cookie)-1) :
        left = mid
        right = mid+1
        left_sum = cookie[left]
        right_sum = cookie[right]
        
        while True :
            if left_sum == right_sum :
                ans = max(ans, left_sum)
                if left == 0 or right == len(cookie)-1 : break
                left -= 1
                left_sum += cookie[left]
                right += 1
                right_sum += cookie[right]
            elif left_sum > right_sum :
                if right == len(cookie)-1 : break
                right += 1
                right_sum += cookie[right]
            else :
                if left == 0 : break
                left -= 1
                left_sum += cookie[left]
    return ans
            