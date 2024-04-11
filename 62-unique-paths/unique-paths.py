class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cols = n * [0]
        cols[-1] = 1 # 1 way for bottom right cell to reach itself

        for i in range(m):
            for j in reversed(range(n - 1)):
                cols[j] = cols[j] + cols[j + 1]

        return cols[0]
        