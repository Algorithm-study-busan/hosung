import random
class RandomizedSet:
    def __init__(self):
        self.arr = list()
        self.idx = dict()

    def insert(self, val: int) -> bool:
        if val in self.idx.keys() :
            return False 
        else :
            self.arr.append(val)
            self.idx[val] = len(self.arr)-1
            return True

    def remove(self, val: int) -> bool:
        if val in self.idx.keys() :
            i = self.idx[val]
            del self.idx[val]
            temp = self.arr[-1]
            self.arr[i] = temp
            self.arr.pop(-1)
            if val != temp :
                self.idx[temp]=i
            return True
        else :
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()