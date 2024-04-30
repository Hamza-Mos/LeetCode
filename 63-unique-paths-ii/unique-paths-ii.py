class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        # target cell is unreachable (obstacle)
        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        dp = [0] * COLS
        dp[-1] = 1 # 1 way to reach target cell if starting at target cell

        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                # obstacle
                if obstacleGrid[i][j]:
                    dp[j] = 0
                    continue

                if j + 1 < COLS:
                    dp[j] += dp[j + 1]

        return dp[0]
                
        