class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # need to find the lowest one, highest one, rightmost one, leftmost one and form a rectangle
        top = left = float('inf')
        bottom = right = float('-inf')

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    top = min(row, top)
                    left = min(col, left)
                    bottom = max(row, bottom)
                    right = max(col, right)


        return (bottom - top + 1) * (right - left + 1)
        