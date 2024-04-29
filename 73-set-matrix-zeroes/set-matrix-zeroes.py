class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        firstRow = False

        # use leftmost column and top row to mark zeroes
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0:
                        firstRow = True

                    else:
                        matrix[row][0] = 0

                    matrix[0][col] = 0

        # set zeroes for everything except first row and first column
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # set zeroes for first column
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        # set zeroes for first row
        if firstRow:
            for col in range(COLS):
                matrix[0][col] = 0
        