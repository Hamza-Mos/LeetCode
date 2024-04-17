class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        numFresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                # fresh
                if grid[i][j] == 1:
                    numFresh += 1

                # rotten
                elif grid[i][j] == 2:
                    q.append([i, j])

        while q and numFresh:
            currLevelLen = len(q)

            for i in range(currLevelLen):
                row, col = q.popleft()

                for x, y in directions:
                    if 0 <= row + x < ROWS and 0 <= col + y < COLS and grid[row + x][col + y] == 1:
                        grid[row + x][col + y] = 2
                        numFresh -= 1
                        q.append([row + x, col + y])

            time += 1

        return time if numFresh == 0 else -1        