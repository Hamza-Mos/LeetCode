class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        
        # can only move right or down
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # [time, row, col]
        minHeap = [[grid[0][0], 0, 0]]
        visited = set()

        while minHeap:
            currTime, row, col = heapq.heappop(minHeap)

            # have reached target cell
            if (row, col) == (ROWS - 1, COLS - 1):
                return currTime

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for x, y in directions:
                if 0 <= row + x < ROWS and 0 <= col + y < COLS and (row + x, col + y) not in visited:
                    time = max(grid[row + x][col + y], currTime)
                    heapq.heappush(minHeap, [time, row + x, col + y])

        return -1
        