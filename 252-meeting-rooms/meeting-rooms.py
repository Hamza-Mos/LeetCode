class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # if there is any overlap, return False
        # else, return True
        if not intervals:
            return True

        intervals.sort()

        lastEnd = intervals[0][1]

        for index in range(1, len(intervals)):
            start, end = intervals[index]

            if lastEnd > start:
                return False

            lastEnd = end

        return True
        