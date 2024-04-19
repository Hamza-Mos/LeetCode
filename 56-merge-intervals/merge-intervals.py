class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort()

        res = [intervals[0]]

        for i in range(len(intervals)):
            start, end = intervals[i]

            # this interval comes after the last interval in our res list (no overlap)
            if start > res[-1][1]:
                res.append(intervals[i])

            # overlap
            else:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]

        return res