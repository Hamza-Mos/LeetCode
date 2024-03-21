class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        inf = 2147483647
        ROWS, COLS = len(rooms), len(rooms[0])

        # do bfs from gates outwards
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                # if it is a gate then add coordinates to q
                if rooms[i][j] == 0:
                    # (row, col, distance to nearest gate)
                    q.append((i, j, 0))


        # bfs
        while q:
            row, col, distance = q.popleft()

            for x, y in directions:
                # adjacent cell is within bounds and represents an empty room
                if 0 <= row + x < ROWS and 0 <= col + y < COLS and rooms[row + x][col + y] == inf:
                    # increment distance by 1 and append to queue
                    rooms[row + x][col + y] = distance + 1
                    q.append((row + x, col + y, distance + 1))