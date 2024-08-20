class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        refresher on matrix multiplication

        mat1 = [
            a1  b1

            c1  d1
        ]

        mat2 = [
            a2  b2

            c2  d2
        ]

        element from mat1 with coordinates (x1, y1) and element from mat2 with coordinates (x2, y2)
        will contribute to dot product for value at coordinate (x1, y2) in mat3

        mat3 = [
            (row1 from mat1 * col1 from mat2)   (row1 from mat1 * col2 from mat2)

            (row2 from mat1 * col1 from mat2)   (row2 from mat1 * col2 from mat2)
        ]

        therefore:
        
        mat3 = [
            (a1 b1) * (a2 c2)   (a1 b1) * (b2 d2)

            (c1 d1) * (a2 c2)   (c1 d1) * (b2 d2)
        ]

        mat3 = [
            [a1a2 + b1c2]   [a1b2 b1d2]

            [c1a2 + d1c2]   [c1b2 d1d2]
        ]

        also if mat1 has dimensions m x k and mat2 has dimensions k x n then mat3 must have dimensions m x n

        """


        """

        2 approaches:

        1) brute force where you create a matrix with dimensions m x n where all cells have a value of 0
           and then loop over elements from both matrices and follow the formula

        2) create a function to compress the matrices and only include numbers in each row if they are non-zero

        NOTE: remember that dimensions are m x k and k x n for the matrices respectively.
              so for looping, you can loop over each element in mat1 and use the element's column 
              to loop over the elements in mat2[column] since you can use mat1's columns as row indices
              for mat2

        """

        m = len(mat1) # rows of final matrix
        k = len(mat1[0])
        n = len(mat2[0]) # cols of final matrix

        res = [[0] * n for row in range(m)]

        # function to compress_matrix to only non-zero elements
        def compress_matrix(matrix):
            rows = len(matrix)
            cols = len(matrix[0])

            compressed_matrix = [[] for row in range(rows)]

            for row_index, row_elements in enumerate(matrix):
                for col_index, val in enumerate(row_elements):
                    # only add non-zero elements
                    if val:
                        compressed_matrix[row_index].append((val, col_index)) # need to keep track of col index for multiplication


            return compressed_matrix

        compressed_mat1 = compress_matrix(mat1)
        compressed_mat2 = compress_matrix(mat2)

        for row_index, row_elements in enumerate(compressed_mat1):
            for val1, index in row_elements:
                for val2, col_index in compressed_mat2[index]:
                    res[row_index][col_index] += val1 * val2

        return res