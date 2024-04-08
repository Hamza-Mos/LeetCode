class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ROWS = COLS = len(matrix)

        # intuition behind this problem is to be greedy since we can always shift negatives around until they
        # are adjacent

        # if count of negatives is even then we can just transform all of them to positive and get max sum

        # if count is odd then we can greedily find the smallest negative value (smallest in magnitude)
        # then return total absolute sum - 2*smallestNum


        # count number of negatives
        negatives = 0

        # track smallest negative (in magnitude)
        smallest = float('inf')

        # total absolute sum
        total = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] < 0:
                    negatives += 1

                total += abs(matrix[i][j])

                smallest = min(smallest, abs(matrix[i][j]))

        return total if negatives % 2 == 0 else total - 2*smallest