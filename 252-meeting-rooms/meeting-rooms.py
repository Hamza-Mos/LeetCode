class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        prevEnd = -1

        for start, end in intervals:
            if start < prevEnd:
                return False

            prevEnd = end

        return True
        