class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        # algorithm overview:

        # **REVERSE THINKING**
        # instead of approaching this problem by capturing all surrounded regions,
        # we can be a bit more clever and approach this problem by capturing everything BUT unsurrounded regions!
        # We will do this by marking all O's that cannot be flipped (either at the border or beside another O
        # that cannot be flipped).

        # steps:
        
        # 1. call dfs and mark all non-flippable O's by converting them into T's
        # 2. loop over whole board and convert the flippable O's to X's and T's (non-flippable O's) back to O's

        # dfs function to mark non-flippable O's
        def capture(row, col):
            # out of bounds or not an "O"
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != "O":
                return

            # convert to T
            board[row][col] = "T"

            # visit neighbouring cells
            capture(row + 1, col)
            capture(row - 1, col)
            capture(row, col + 1)
            capture(row, col - 1)

        # step 1: mark all non-flippable O's (starting at the border)
        # bottom and top rows
        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)

        # left and right columns
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)

        # step 2: loop over whole board and convert the flippable O's to X's and T's (non-flippable O's) back to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"
        