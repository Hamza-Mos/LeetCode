class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rows = [[float('inf')] * (COLS + 1) for i in range(ROWS + 1)]
        rows[ROWS][COLS - 1] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                rows[row][col] = min(
                    rows[row][col], 
                    rows[row][col + 1] + grid[row][col], 
                    rows[row + 1][col] + grid[row][col]
                )

        return rows[0][0]

        