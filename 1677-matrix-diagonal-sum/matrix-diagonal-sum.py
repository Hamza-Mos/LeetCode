class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                # check if its in a diagonal
                # negative diagonal: row == col
                # positive diagonal: row + col == N - 1
                if row == col or row + col == len(mat) - 1:
                    res += mat[row][col]

        return res 
        