class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                return 0

            # mark as visited by marking cell as water and not land
            grid[row][col] = 0

            # returns island area
            return 1 + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        
        return res