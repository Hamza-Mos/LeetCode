class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # find row
        low, high = 0, ROWS - 1
        row = -1

        while low <= high:
            mid = (low + high) // 2

            # find if target exists in current row
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break

            elif matrix[mid][0] < target:
                low = mid + 1

            else:
                high = mid - 1

        # no row could contain target
        if row == -1:
            return False

        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        