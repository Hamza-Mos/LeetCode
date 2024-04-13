class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        maxLeft = maxRight = 0
        left, right = 0, len(height) - 1

        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if height[left] < height[right]:

                left += 1

                currHeightGains = min(maxLeft, maxRight) - height[left]

                res = res + currHeightGains if currHeightGains > 0 else res

            else:

                right -= 1

                currHeightGains = min(maxLeft, maxRight) - height[right]

                res = res + currHeightGains if currHeightGains > 0 else res

        return res

        