class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.valToIndex = defaultdict(set)
        

    def insert(self, val: int) -> bool:

        self.valToIndex[val].add(len(self.list))
        self.list.append(val)

        return len(self.valToIndex[val]) == 1
        

    def remove(self, val: int) -> bool:
        if len(self.valToIndex[val]) == 0:
            return False

        lastVal, indexToRemove = self.list[-1], self.valToIndex[val].pop()

        self.list[indexToRemove] = lastVal
        self.valToIndex[lastVal].add(indexToRemove)
        self.valToIndex[lastVal].remove(len(self.list) - 1) 

        self.list.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()