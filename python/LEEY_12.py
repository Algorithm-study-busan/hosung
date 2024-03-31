class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [['M'], ['C','D','M'], ['X', 'L', 'C'], ['I', 'V', 'X']]

        ans = ""

        for i in range(len(str(num))) :
            n = int(str(num)[i]) 
            k = i + 4 - len(str(num))
            if n <= 3 :
                ans += arr[k][0] * n
            elif n == 4 : 
                ans += arr[k][0] + arr[k][1]
            elif n <= 8 :
                ans += arr[k][1] + arr[k][0] * (n % 5)
            else :
                ans += arr[k][0] + arr[k][2]
        
        return ans