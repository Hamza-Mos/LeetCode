class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create an empty board
        board = [["."] * n for i in range(n)]

        res = []

        cols = set()
        posDiag = set()
        negDiag = set()

        def dfs(row):
            # we have reached the end of the board successfully (meaning that we have completed one solution)
            if row == n:
                # generate a copy of the board and add it to result list
                copy = ["".join(board[row]) for row in range(n)]
                res.append(copy)

            # try every possible column position in the current row
            for col in range(n):
                # row + col is always a constant in positive diag because row decreases as you go diagonally
                # while col number increases 
                curPosDiag = row + col

                # row - col is always a constant in negative diag because both row and col always increase by 1
                # each time
                curNegDiag = row - col

                # invalid position
                if col in cols or curPosDiag in posDiag or curNegDiag in negDiag:
                    continue

                # valid position so mark it as taken in sets
                cols.add(col)
                posDiag.add(curPosDiag)
                negDiag.add(curNegDiag)

                board[row][col] = "Q"

                # call dfs on next row
                dfs(row + 1)

                # backtrack (unvisit the cell)
                cols.remove(col)
                posDiag.remove(curPosDiag)
                negDiag.remove(curNegDiag)

                board[row][col] = "."
                
        
        dfs(0)

        return res
        