class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.numsToIndex = {}

    def insert(self, value):
        if value in self.numsToIndex:
            return False
        
        self.nums.append(value)
        self.numsToIndex[value] = len(self.nums) - 1

        return True

    def remove(self, value):
        if value not in self.numsToIndex:
            return False
        
        indexToRemove, lastNum = self.numsToIndex[value], self.nums[-1]
        self.nums[indexToRemove], self.numsToIndex[lastNum] = lastNum, indexToRemove

        del self.numsToIndex[value]
        self.nums.pop()

        return True

    def getRandom(self):
        return choice(self.nums)