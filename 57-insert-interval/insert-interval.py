class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # key to this problem is to find the point where newInterval overlaps with any interval in the list

        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            # newInterval ends before this interval (we can return)
            if newInterval[1] < start:
                return res + [newInterval] + intervals[i:]

            # newInterval comes after this interval
            elif end < newInterval[0]:
                res.append(intervals[i])

            # overlap
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]

        # if we have not returned yet at this point then that means newInterval is the last interval we need to add
        return res + [newInterval]
        