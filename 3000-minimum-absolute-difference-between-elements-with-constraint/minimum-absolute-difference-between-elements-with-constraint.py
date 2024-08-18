from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sortedWindow = SortedList()  # Maintain a sorted list of elements within the window
        minDifference = float('inf')  # Initialize result with infinity
        
        # Iterate over the array with index current representing the current element
        # start from x to ensure the window size is at least minDistance
        for currentIndex in range(x, n):
            sortedWindow.add(nums[currentIndex - x])
            
            # Perform binary search to find the position to insert nums[currentIndex] in sortedWindow
            insertPosition = sortedWindow.bisect_left(nums[currentIndex])
            
            # Check the closest values around the insertion point
            for nearbyIndex in [insertPosition - 1, insertPosition]:
                if 0 <= nearbyIndex < len(sortedWindow):  # Ensure nearbyIndex is within bounds
                    minDifference = min(minDifference, abs(nums[currentIndex] - sortedWindow[nearbyIndex]))
        
        return minDifference  # Return the minimum absolute difference found