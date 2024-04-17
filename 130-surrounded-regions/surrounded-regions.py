class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return

            if board[row][col] == "T" or board[row][col] == "X":
                return

            board[row][col] = "T"

            for x, y in directions:
                dfs(row + x, col + y)

        # go over borders to capture the unsurrounded regions
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"

        
        