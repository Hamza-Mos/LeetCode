class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        left = leftMax = rightMax = 0
        right = len(height) - 1

        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)

            if height[left] < height[right]:
                res += max(0, min(leftMax, rightMax) - height[left])
                left += 1

            else:
                res += max(0, min(leftMax, rightMax) - height[right])
                right -= 1
            
        return res