class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start times
        intervals.sort()

        res = [intervals[0]]

        for index in range(1, len(intervals)):
            start, end = intervals[index]
            # no overlap
            if res[-1][1] < start:
                res.append(intervals[index])

            # overlap
            else:
                # update the end time of last interval
                # start times are already taken care of cuz intervals is sorted by start time (so start time is always
                # minimized)
                res[-1][1] = max(end, res[-1][1])

        return res

        