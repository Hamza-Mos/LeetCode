class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col, visitSet, prevHeight):
            # out of bounds or already visited
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visitSet:
                return

            # we must move to greater or equal heights (going backwards)
            # so if prevHeight is greater than current height then this is an invalid path
            if prevHeight > heights[row][col]:
                return

            visitSet.add((row, col))

            for x, y in directions:
                dfs(row + x, col + y, visitSet, heights[row][col])

        # top row -> pacific
        # bottom row -> atlantic
        for col in range(COLS):
            dfs(0, col, pacific, -1)
            dfs(ROWS - 1, col, atlantic, -1)

        # leftmost col -> pacific
        # rightmost col -> atlantic
        for row in range(ROWS):
            dfs(row, 0, pacific, -1)
            dfs(row, COLS - 1, atlantic, -1)

        return pacific & atlantic
        