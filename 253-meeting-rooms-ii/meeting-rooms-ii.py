class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []

        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))

        times.sort()

        currMeetings = maxMeetings = 0

        for time, addition in times:
            currMeetings += addition

            maxMeetings = max(currMeetings, maxMeetings)

        return maxMeetings