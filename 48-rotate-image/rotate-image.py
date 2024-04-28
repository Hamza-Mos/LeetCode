class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n x n matrix so the top and bottom boundaries will be same as left & right
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                topLeft, topRight, bottomRight, bottomLeft = matrix[top][left + i], matrix[top + i][right], matrix[bottom][right - i], matrix[bottom - i][left]

                matrix[top][left + i] = bottomLeft
                matrix[top + i][right] = topLeft
                matrix[bottom][right - i] = topRight
                matrix[bottom - i][left] = bottomRight

            left += 1
            right -= 1

        