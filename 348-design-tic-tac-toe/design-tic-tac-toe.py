class TicTacToe:
    # player 1 - positive
    # player 2 - negative
    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n

        # diag formula: (row - col == 0)
        self.diag = 0

        # reverse diag formula: (row + col == n - 1)
        self.reverseDiag = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        point = 1 if player == 1 else -1
        n = len(self.rows)

        self.rows[row] += point
        self.cols[col] += point

        # check diagonals
        if row - col == 0:
            self.diag += point

        if row + col == n - 1:
            self.reverseDiag += point

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diag) == n or abs(self.reverseDiag) == n:
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)