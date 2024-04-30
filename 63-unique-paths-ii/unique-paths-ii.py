class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        # target cell is unreachable (obstacle)
        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        dp = [0] * COLS
        dp[-1] = 1 # 1 way to reach target cell if starting at target cell

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                # obstacle
                if obstacleGrid[row][col]:
                    dp[col] = 0
                    continue

                if col + 1 < COLS:
                    dp[col] += dp[col + 1]

        return dp[0]
                
        