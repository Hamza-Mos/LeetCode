from functools import cache
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        @cache
        def dfs(i, j): 
            # last cell in the grid
            if i == m - 1 and j == n - 1: 
                return grid[i][j], grid[i][j]

            # out of bounds
            if i >= m or j >= n: 
                return None, None 
            
            # explore paths
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            
            products = []
            for path in [down, right]:
                if path[0] is not None:
                    products.extend([path[0] * grid[i][j], path[1] * grid[i][j]])
            
            return max(products), min(products) # max and min values in path starting at (i, j)
        
        result = dfs(0, 0)

        if result[0] < 0:
            return -1

        return result[0] % MOD