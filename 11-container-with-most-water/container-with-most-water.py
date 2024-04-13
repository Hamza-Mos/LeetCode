class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            currArea = min(height[left], height[right]) * (right - left)

            maxArea = max(currArea, maxArea)

            if height[left] > height[right]:
                right -= 1

            else:
                left += 1

        return maxArea
        