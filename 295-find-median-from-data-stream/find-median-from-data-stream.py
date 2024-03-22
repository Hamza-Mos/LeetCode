class MedianFinder:

    # 6, 10, 2, 6, 4, 0, 6, 3, 1, 0, 0

    # small: 2, 6

    # large: 10

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if self.small and num < -1 * self.small[0]:
            heapq.heappush(self.small, -num)

        else:
            heapq.heappush(self.large, num)

        

        if len(self.small) > len(self.large) + 1:
            n = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, n)

        elif len(self.large) > len(self.small) + 1:
            n = heapq.heappop(self.large)
            heapq.heappush(self.small, -n)
        

    def findMedian(self) -> float:
        if (len(self.large) + len(self.small)) % 2 == 0:
            biggestSmall = -1 * self.small[0]
            smallestLarge = self.large[0]

            return (biggestSmall + smallestLarge) / 2

        else:
            if len(self.large) > len(self.small):
                return self.large[0]

            else:
                return -1 * self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()