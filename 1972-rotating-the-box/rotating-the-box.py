class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotated_box = [list(reversed(column)) for column in zip(*box)]

        """
        - The zip() function is used to combine elements from multiple iterables (like lists, tuples, etc.) 
          into tuples.

        ex:
            box = [
                    ['#', '.', '#'],
                    ['#', '#', '*'],
                    ['.', '.', '.']
                ]

            list(zip(box)) = [
                            (['#', '.', '#'],),
                            (['#', '#', '*'],),
                            (['.', '.', '.'],)
                        ]

        - The * operator is used in Python to unpack the elements of a list (or any iterable). 
          When you use *box, it unpacks the list box into individual elements.

        ex:
            box = [
                    ['#', '.', '#'],
                    ['#', '#', '*'],
                    ['.', '.', '.']
                ]

            zip(*box) = zip(['#', '.', '#'], ['#', '#', '*'], ['.', '.', '.'])

            **Basically gets rid of the outermose layer in the matrix and breaks down into individual lists**

        - zip(*box) transposes the matrix (box). It groups elements from each row together into columns.
          (basically first row becomes first column)
        - reversed(column) then reverses each column (which originally was a row), effectively rotating 
          the matrix 90 degrees clockwise.
        - The list comprehension wraps everything into a list of lists, creating the rotated matrix.

        for example, box is:
            box = [
                    ['#', '.', '#'],
                    ['#', '#', '*'],
                    ['.', '.', '.']
                ]

        after zip(*box), box is:
            box = [
                    ('#', '#', '.'),
                    ('.', '#', '.'),
                    ('#', '*', '.')
                ]


        after applying reversed(column), box is:
            box = [
                    ['.', '#', '#'],
                    ['#', '#', '.'],
                    ['.', '*', '#']
                ]

        """

        """
        approach:

        - rotate the box (using zip(*box))
        - loop over each column
            - go through each element and check if it is a stone, obstacle, or empty and count number of stones
                - if empty, then don't do anything
                - if it a stone, then increment number of stones and assign current cell to be empty
                - if it is an obstacle, set all previous stone cells in the column to be stones and
                  reset the stone counter (keep looping through the rest of the column because there 
                  could be more stones afterwards)

            - once done looping over the column, then set all last stone cells in the columns to stones
              if stone counter is > 0
        """

        # fall due to gravity
        rows, cols = len(rotated_box), len(rotated_box[0])
        for c in range(cols):
            stones = 0
            for r in range(rows):
                if rotated_box[r][c] == '.': # empty
                    continue
                if rotated_box[r][c] == '#': # stone
                    stones += 1
                    rotated_box[r][c] = '.'
                    continue
                for i in range(stones): # obstacle
                    # set all previous cells to stones and reset stone counter
                    rotated_box[r - 1 - i][c] = '#'
                stones = 0

            # set all previous cells to stones if stones > 0
            if stones:
                for i in range(stones):
                    rotated_box[r - i][c] = '#'
        
        return rotated_box