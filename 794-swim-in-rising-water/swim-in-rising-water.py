class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]] # time, row, col
        visited = set()

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if (row, col) in visited:
                continue

            if (row, col) == (ROWS - 1, COLS - 1):
                return time

            visited.add((row, col))

            for x, y in directions:
                if 0 <= row + x < ROWS and 0 <= col + y < COLS and (row + x, col + y) not in visited:
                    newTime = max(time, grid[row + x][col + y])
                    heapq.heappush(minHeap, [newTime, row + x, col + y])

            
        