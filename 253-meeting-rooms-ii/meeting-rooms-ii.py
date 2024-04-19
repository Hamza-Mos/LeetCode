class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []

        for start, end in intervals:
            times.append([start, 1]) 
            times.append([end, -1])

        # sort by times
        times.sort()
        numMeetings = 0
        maxMeetings = 0

        print(times)

        for time, addition in times:
            numMeetings += addition
            maxMeetings = max(numMeetings, maxMeetings)

        return maxMeetings
        