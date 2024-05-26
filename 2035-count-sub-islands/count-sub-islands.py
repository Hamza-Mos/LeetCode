class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        res = 0

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid2[row][col] == 0:
                return True

            # mark as visited
            grid2[row][col] = 0
            
            # even if current cell in grid1 is water, we should still visit the rest of the island in grid2
            # to mark it as visited
            res = grid1[row][col] == 1

            # Perform DFS in all four directions
            res &= dfs(row + 1, col)
            res &= dfs(row - 1, col)
            res &= dfs(row, col + 1)
            res &= dfs(row, col - 1)

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1

        return res
        