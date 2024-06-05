class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        row, col = ROWS - 1, 0

        while row >= 0 and col < COLS:
            if matrix[row][col] == target:
                return True

            # need to move to a lower number
            elif matrix[row][col] > target:
                row -= 1

            # move to higher number
            else:
                col += 1

        return False