class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set() # keeps track of used columns
        diagSet = set() # keeps track of used positive diagonals (remember (r + c) stays constant)
        reverseDiagSet = set() # keeps track of used anti diagonals (remember (r - c) stays constant)

        board = [ ["."] * n for i in range(n) ]
        res = []

        def backtrack(currRow):
            if currRow == n:
                currBoard = []
                for i in range(n):
                    currRow = "".join(board[i].copy())
                    currBoard.append(currRow)

                res.append(currBoard)
                return

            for col in range(n):
                if col in colSet or (currRow + col) in diagSet or (currRow - col) in reverseDiagSet:
                    continue

                colSet.add(col)
                diagSet.add(currRow + col)
                reverseDiagSet.add(currRow - col)

                board[currRow][col] = "Q"

                backtrack(currRow + 1)

                board[currRow][col] = "."

                # backtrack
                colSet.remove(col)
                diagSet.remove(currRow + col)
                reverseDiagSet.remove(currRow - col)

        backtrack(0)

        return res