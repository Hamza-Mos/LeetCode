from functools import cache
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        @cache
        def dfs(i, j): 
            """Return maximum & minimum products starting at (i, j)."""
            if i == m - 1 and j == n - 1: 
                return grid[i][j], grid[i][j]
            if i >= m or j >= n: 
                return None, None  # Use None instead of infinity
            
            # Recursive calls to explore the next cells (down and right)
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            
            if down[0] is None and right[0] is None:
                return None, None
            
            products = []
            for path in [down, right]:
                if path[0] is not None:
                    products.extend([path[0] * grid[i][j], path[1] * grid[i][j]])
            
            return max(products), min(products)
        
        result = dfs(0, 0)
        if result[0] is None or result[0] < 0:
            return -1
        return result[0] % MOD