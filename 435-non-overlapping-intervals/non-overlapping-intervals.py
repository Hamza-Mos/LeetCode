class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)

        numToRemove = 0
        prevStart, prevEnd = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # overlap
            if start < prevEnd:
                numToRemove += 1
                prevEnd = min(prevEnd, end)

            else:
                prevEnd = end

        return numToRemove
        