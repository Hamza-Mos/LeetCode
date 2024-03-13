class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col, index):
            # we found a match
            if index == len(word):
                return True
            
            # out of bounds, already visited, or wrong character
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] == "." or board[row][col] != word[index]:
                return False

            curChar = board[row][col]
            
            # mark as visited
            board[row][col] = "."

            # explore neighbouring cells
            for x, y in directions:
                if dfs(row + x, col + y, index + 1):
                    return True

            # backtrack
            board[row][col] = curChar

            return False

        # call dfs starting from each cell
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False