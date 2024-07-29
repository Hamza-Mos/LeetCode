class FreqStack:
    def __init__(self):
        self.maxFreq = 0 # max frequency in the stack at any point
        self.valsMap = defaultdict(list) # maps a frequency to a list of values with that frequency (maintains order of insertion)
        self.freqMap = defaultdict(int) # maps a number to its frequence
        

    def push(self, val: int) -> None:
        self.freqMap[val] += 1

        self.maxFreq = max(self.maxFreq, self.freqMap[val])
        
        self.valsMap[self.freqMap[val]].append(val)
        

    def pop(self) -> int:
        # update the max frequency (if list is empty, then that frequency does not have any elements)
        # so we keep decrementing until we get to a frequency that has items (frequency that is valid)
        while not self.valsMap[self.maxFreq]:
            self.maxFreq -= 1

        val = self.valsMap[self.maxFreq].pop()

        self.freqMap[val] -= 1 # update the value's frequency

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()