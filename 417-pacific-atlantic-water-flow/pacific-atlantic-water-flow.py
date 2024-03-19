class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # dfs function to explore cells that can travel to ocean
        def dfs(row, col, oceanSet, prevHeight):
            # already visited, out of bounds, or invalid (prev height is greater than current height)
            if (row, col) in oceanSet or row < 0 or row >= ROWS or col < 0 or col >= COLS or heights[row][col] < prevHeight:
                return

            # mark as visited
            oceanSet.add((row, col))

            curHeight = heights[row][col]

            # explore all other neighbouring cells
            dfs(row + 1, col, oceanSet, curHeight)
            dfs(row - 1, col, oceanSet, curHeight)
            dfs(row, col + 1, oceanSet, curHeight)
            dfs(row, col - 1, oceanSet, curHeight)

        # start at the top (pacific) and bottom (atlantic) rows and go as deep as you can with dfs
        # mark each cell as visited

        # if a cell is marked as visited by one of the ocean sets then it means that cell can reach that ocean

        # we are working backwards (from ocean to cells and not from all possible cells to ocean to save time 
        # complexity). so previous height must be less than or equal to current height (since we go backwards)

        # dfs on rows (top and bottom):
        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)

        # same thing but for columns (leftmost for pacific and rightmost for atlantic)
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)

        # if a cell is in both ocean visited cells then that means that cell can reach both oceans and we
        # should return it as part of our output list

        # '&' operator is a shortcut - returns all elements in the intersection of both sets (in common between 
        # both sets)
        return pac & atl