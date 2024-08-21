from bisect import bisect_left, bisect_right
from math import inf

class CountIntervals:

    def __init__(self):
        # Initialize the list of intervals with sentinel values to simplify edge case handling
        self.intervals = [(-inf, -inf), (inf, inf)]
        # Initialize the total coverage of all intervals
        self.total_coverage = 0   

    def add(self, left: int, right: int) -> None:
        """
        time complexity: O(log n + m)

        where n is the number of intervals in self.intervals
        where m is the number of intervals between left_index and right_index (calculating coverage to remove)

        """
        # Reference to the intervals list for easier access
        intervals = self.intervals
        
        # Find the left-most position to insert the new interval or merge with existing ones.
        # We use `left - 1` because interval boundaries are inclusive.
        left_index = bisect_left(intervals, left - 1, key=lambda x: x[1])
        # Determine the minimum left boundary of the merged interval
        merged_left = min(intervals[left_index][0], left)
        
        # Find the right-most position to insert the new interval or merge with existing ones.
        # We use `right + 1` because interval boundaries are inclusive.
        right_index = bisect_right(intervals, right + 1, key=lambda x: x[0])
        # Determine the maximum right boundary of the merged interval
        merged_right = max(intervals[right_index - 1][1], right)

        # Calculate the total coverage of the intervals that will be replaced by the new merged interval
        coverage_to_remove = 0
        for i in range(left_index, right_index):
            coverage_to_remove += intervals[i][1] - intervals[i][0] + 1
            
        # Update the total coverage by adding the coverage of the new interval
        # and subtracting the coverage of the replaced intervals
        self.total_coverage += (merged_right - merged_left + 1) - coverage_to_remove
        
        # Replace the old intervals with the new merged interval
        intervals[left_index:right_index] = [(merged_left, merged_right)]

    def count(self) -> int:
        # Return the current total coverage of all intervals
        return self.total_coverage

        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()