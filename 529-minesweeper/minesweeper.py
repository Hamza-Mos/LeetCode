class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        conditions for cells:

        1) current cell is a mine (M) -> change to X
        2) current cell is an unrevealed empty square:
            a) there are adjacent mines -> change to digit
            b) there are no adjacent mines -> change to B
        """
        directions = [[1, 0], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1], [0, -1], [-1, 0]]
        ROWS, COLS = len(board), len(board[0])

        # return 1 if an unrevealed mine is found
        # return 0 otherwise
        def dfs(row, col):
            # out of bounds
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0

            # revealed already
            if board[row][col] == "B" or board[row][col] in "12345678":
                return 0

            # check if it is a mine
            if board[row][col] == "M":
                return 1

            adjacentUnrevealedEmptySquares = []

            # unrevealed empty square
            numMinesFound = 0
            for x, y in directions:
                # within bounds
                if 0 <= row + x < ROWS  and 0 <= col + y < COLS:
                    # check for mines
                    if board[row + x][col + y] == "M":
                        numMinesFound += 1

                    # another unrevealed square
                    elif board[row + x][col + y] == "E":
                        adjacentUnrevealedEmptySquares.append([row + x, col + y])

            # adjacent mine found
            if numMinesFound:
                board[row][col] = str(numMinesFound)

            # call dfs on adjacent unrevealed empty squares
            else:
                board[row][col] = "B"

                for cellX, cellY in adjacentUnrevealedEmptySquares:
                    dfs(cellX, cellY)

            # return 0 because this is an empty square
            return 0
                

        # if a mine was clicked, change to X and return
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        # otherwise, call dfs with clicked row, col
        dfs(click[0], click[1])

        return board
        