# USE SORTED SET!!
from sortedcontainers import SortedSet

class SummaryRanges:

    def __init__(self):
        self.nums = SortedSet() # so you can iterate over numbers in sorted order
        

    def addNum(self, value: int) -> None:
        self.nums.add(value) # O(log n) operation
        

    def getIntervals(self) -> List[List[int]]:
        res = []

        for n in self.nums:
            # if the current number belongs to previous interval in res
            # meaning that current number == 1 + last number
            # then update the latest interval
            if res and n == res[-1][1] + 1:
                res[-1][1] = n

            # otherwise, add a new interval to the list
            else:
                res.append([n, n])

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()