class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0

        if m * n != r * c:
            return mat

        flatList = [item for sublist in mat for item in sublist]

        # Create the reshaped matrix
        newMatrix = []

        for i in range(r):
            newMatrix.append(flatList[i * c:(i + 1) * c])

        return newMatrix