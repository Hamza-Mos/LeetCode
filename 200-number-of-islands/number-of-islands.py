class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col):
            # out of bounds or not land
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            # check neighbouring cells
            for x, y in directions:
                dfs(row + x, col + y)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res
        