class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort() # sort by start time

        prevEnd = -1

        for start, end in intervals:
            # overlap (current meeting starts before the previous one ended)
            if start < prevEnd:
                return False

            prevEnd = end

        return True
        