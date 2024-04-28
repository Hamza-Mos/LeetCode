class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        left = top = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # go across top (left to right)
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1

            # go across rightmost column (top to bottom)
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])

            right -= 1

            # edge case where inner matrix is a single row and top > bottom
            if top > bottom: break

            # edge case where inner matrix is a single column and left > right
            if left > right: break

            # go across bottom row (right to left)
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])

            bottom -= 1

            # go across leftmost column (bottom to top)
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])

            left += 1

        return res
        