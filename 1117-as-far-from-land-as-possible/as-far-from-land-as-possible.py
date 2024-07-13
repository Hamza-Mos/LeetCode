class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # bfs
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS = COLS = len(grid)
        visited = set()
        res = 0

        # find all water cells and add then to a queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    q.append((r, c, 0))
                    visited.add((r, c))

        # no land
        if not q or not visited:
            return -1

        # no water
        if len(q) == ROWS * COLS:
            return -1

        while q:
            row, col, dist = q.popleft()

            res = max(dist, res)

            for x, y in directions:
                if 0 <= row + x < ROWS and 0 <= col + y < COLS and (row + x, col + y) not in visited:
                    visited.add((row + x, col + y))
                    q.append((row + x, col + y, dist + 1))

        return res


                
        