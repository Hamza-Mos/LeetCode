class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        row = ROWS - 1
        col = 0

        # keep traversing right until we hit a number that is greater than our target (move to larger numbers)
        # then we keep traversing up until we hit a number less than our target (move to smaller numbers)
        # repeat until we end loop or reach target

        while row >= 0 and col < COLS:
            # found target
            if matrix[row][col] == target:
                return True

            # current number is less than target so we move right to larger numbers
            elif matrix[row][col] < target:
                col += 1

            # current number is greater than target so we move up to smaller numbers
            else:
                row -= 1

        return False
            
        