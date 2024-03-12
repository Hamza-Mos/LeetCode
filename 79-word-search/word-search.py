class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, index):
            if index >= len(word):
                return True
            
            if(row not in range(ROWS) or col not in range(COLS) or board[row][col] == '.' or board[row][col] != word[index]):
                return False

            currChar = board[row][col]
            # the dot marks the current cell as visited
            board[row][col] = '.'

            # dfs on next cell
            if (dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1)):
                return True

            # mark the cell as unvisited
            board[row][col] = currChar
            return False
            

        # call dfs on each cell in the board
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False