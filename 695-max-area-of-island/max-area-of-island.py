class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        curIslandNumber = -1
        islandMap = {}

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                return

            islandMap[curIslandNumber] += 1
            grid[row][col] = curIslandNumber

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    islandMap[curIslandNumber] = 0
                    dfs(i, j)

                    res = max(islandMap[curIslandNumber], res)
                    curIslandNumber -= 1
        
        return res