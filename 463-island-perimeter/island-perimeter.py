class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for row in range(ROWS):
            for col in range(COLS):
                # land
                if grid[row][col] == 1:
                    # check neighbour cells for land
                    perimeterAdd = 4

                    for x, y in directions:
                        if 0 <= row + x < ROWS and 0 <= col + y < COLS and grid[row + x][col + y] == 1:
                            perimeterAdd -= 1

                    res += perimeterAdd

        return res
        