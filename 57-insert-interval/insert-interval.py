class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for index in range(len(intervals)):
            start, end = intervals[index]

            # newInterval ends before start of current interval
            if newInterval[1] < start:
                return res + [newInterval] + intervals[index:]

            # newInterval starts after current interval
            elif end < newInterval[0]:
                res.append(intervals[index])

            # newInterval overlaps with current interval
            else:
                newStart = min(newInterval[0], start)
                newEnd = max(newInterval[1], end)
                newInterval = [newStart, newEnd]

        return res + [newInterval]
        