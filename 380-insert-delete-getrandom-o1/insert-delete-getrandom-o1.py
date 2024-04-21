class RandomizedSet:

    def __init__(self):
        self.list = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False

        self.valToIndex[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False

        lastVal, indexOfItemToRemove = self.list[-1], self.valToIndex[val]

        # update list and dict
        self.list[indexOfItemToRemove] = lastVal
        self.valToIndex[lastVal] = indexOfItemToRemove
        
        # remove val from list and dict
        self.list.pop()
        del self.valToIndex[val]

        return True

        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()