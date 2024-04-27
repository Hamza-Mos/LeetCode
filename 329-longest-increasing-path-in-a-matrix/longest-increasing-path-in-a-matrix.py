class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        LIP = {} # cache for longest increasing path based on row and col
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col, prevValue):
            # out of bounds
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0

            # invalid (not an increasing path)
            if prevValue >= matrix[row][col]:
                return 0

            # check cache
            if (row, col) in LIP:
                return LIP[(row, col)]

            currValue = matrix[row][col]

            # longest increasing path starting at this cell is 1 (just this cell)
            res = 1

            # check adjacent cells and recursively call dfs
            for x, y in directions:
                res = max(res, 1 + dfs(row + x, col + y, currValue))

            LIP[(row, col)] = res

            return res

        maxLength = 0

        for row in range(ROWS):
            for col in range(COLS):
                maxLength = max(maxLength, dfs(row, col, -1))

        return maxLength

        