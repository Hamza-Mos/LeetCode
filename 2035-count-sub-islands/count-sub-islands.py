class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        res = 0

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid2[row][col] == 0:
                return True
            
            # mark as visited
            grid2[row][col] = 0

            # Check if the corresponding cell in grid1 is water
            is_sub_island = grid1[row][col] == 1

            # Perform DFS in all four directions
            is_sub_island &= dfs(row + 1, col)
            is_sub_island &= dfs(row - 1, col)
            is_sub_island &= dfs(row, col + 1)
            is_sub_island &= dfs(row, col - 1)

            return is_sub_island

        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1

        return res
        