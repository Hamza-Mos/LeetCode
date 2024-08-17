class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])

        # Number of paths from (0, 0) -> (i, j)
        dp1 = [[0] * COLS for i in range(ROWS)]
        dp1[0][0] = 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    if i > 0:
                        dp1[i][j] += dp1[i-1][j]
                    if j > 0:
                        dp1[i][j] += dp1[i][j-1]
        
        # Number of paths from (i, j) -> (ROWS-1, COLS-1)
        dp2 = [[0] * COLS for i in range(ROWS)]

        dp2[ROWS-1][COLS-1] = 1
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if grid[i][j] == 1:
                    if i < ROWS-1:
                        dp2[i][j] += dp2[i+1][j]
                    if j < COLS-1:
                        dp2[i][j] += dp2[i][j+1]
        
        # Number of paths from (0, 0) to (ROWS-1, COLS-1)
        target = dp1[ROWS-1][COLS-1]

        # Check for a critical point (i, j)
        for i in range(ROWS):
            for j in range(COLS):
                if (i != 0 or j != 0) and (i != ROWS-1 or j != COLS-1):
                    if dp1[i][j] * dp2[i][j] == target:
                        return True
        return False
