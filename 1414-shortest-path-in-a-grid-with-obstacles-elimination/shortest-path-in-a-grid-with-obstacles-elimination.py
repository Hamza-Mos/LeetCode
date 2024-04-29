class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        # queue will contain elements (row, col, num obstacles in path)
        queue = deque([(0, 0, 0)])
        target = (ROWS - 1, COLS - 1)
        numSteps = 0
        visit = {(0, 0, 0)}

        while queue:
            currLevelLen = len(queue)

            for i in range(currLevelLen):
                row, col, numObstacles = queue.popleft()

                # invalid path
                if numObstacles > k:
                    continue

                # reached target
                if (row, col) == target:
                    return numSteps

                visit.add((row, col, numObstacles))

                for x, y in directions:
                    # within bounds
                    if 0 <= row + x < ROWS and 0 <= col + y < COLS:
                        newNumObstacles = numObstacles
                        # obstacle
                        if grid[row + x][col + y] == 1:
                            newNumObstacles += 1

                        # cell is already visited with same num obstacles
                        if (row + x, col + y, newNumObstacles) in visit:
                            continue

                        visit.add((row + x, col + y, newNumObstacles))
                        queue.append((row + x, col + y, newNumObstacles))
            
            numSteps += 1

        return -1