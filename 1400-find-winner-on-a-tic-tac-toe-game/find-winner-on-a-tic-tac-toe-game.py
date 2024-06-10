class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # need to keep track of columns, rows, diagonals
        # diagonal: row - col = 0
        # reverse diagonal: row + col == 2

        # player A is +1, playerB is -1
        point = 1

        cols = defaultdict(int)
        rows = defaultdict(int)
        diag = 0
        reverseDiag = 0

        for row, col in moves:
            rows[row] += point
            cols[col] += point

            if row - col == 0:
                diag += point
            
            if row + col == 2:
                reverseDiag += point

            if abs(rows[row]) == 3 or abs(cols[col]) == 3 or abs(diag) == 3 or abs(reverseDiag) == 3:
                return "A" if point == 1 else "B"

            point *= -1

        return "Pending" if len(moves) < 9 else "Draw"
        