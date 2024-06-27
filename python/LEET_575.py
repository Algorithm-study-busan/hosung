class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        check = dict()

        cnt = 0
        for x in candyType :
            if x not in check : 
                cnt += 1
                check[x] = True

        print(cnt)
        return min(cnt, len(candyType)//2)
        