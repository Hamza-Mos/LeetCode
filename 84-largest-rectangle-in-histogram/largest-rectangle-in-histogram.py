class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonically increasing stack
        stack = []
        res = 0

        for index, height in enumerate(heights):
            startIndex = index
            while stack and stack[-1][0] > height:
                prevHeight, startIndex = stack.pop()
                maxArea = prevHeight * (index - startIndex)
                res = max(maxArea, res)

            stack.append([height, startIndex])

        # loop over all remaining elements in stack
        for height, index in stack:
            maxArea = height * (len(heights) - index)
            res = max(maxArea, res)

        return res