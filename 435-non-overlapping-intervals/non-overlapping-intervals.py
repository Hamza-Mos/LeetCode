class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # no overlap
            if lastEnd <= start:
                lastEnd = end

            # overlap
            else:
                res += 1
                lastEnd = min(lastEnd, end)

        return res
        