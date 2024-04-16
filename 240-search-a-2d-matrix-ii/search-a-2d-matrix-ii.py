class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # do binary search on diagonals

        def binarySearch(start, vertical):
            low = start
            high = -1
            # binary search on current col
            if vertical:
                high = ROWS - 1

            # binary search on current row
            else:
                high = COLS - 1

            while low <= high:
                mid = (low + high) // 2

                col = row = -1

                # binary search on row (col does not change)
                if vertical:
                    col = start
                    row = mid

                # same but for col
                else:
                    col = mid
                    row = start

                if matrix[row][col] == target:
                    return True

                elif matrix[row][col] < target:
                    low = mid + 1

                else:
                    high = mid - 1


        for i in range(min(ROWS, COLS)):
            foundTargetInRow = binarySearch(i, False)
            foundTargetInCol = binarySearch(i, True)

            if foundTargetInRow or foundTargetInCol:
                return True

        return False

            
        