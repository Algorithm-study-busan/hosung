class Solution:
    def __init__(self) : 
        self.check = dict()

    def isHappy(self, n: int) -> bool:
        if n == 1 : return True
        if n in self.check : return False
        self.check[n] = 1

        nxt = 0
        for c in str(n) :
            nxt += int(c) ** 2

        return self.isHappy(nxt)
        