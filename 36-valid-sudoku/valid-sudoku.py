class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsMap = defaultdict(set)
        colsMap = defaultdict(set)
        boxMap = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                currNum = board[i][j]

                if currNum == ".":
                    continue

                boxCoordinate = (i // 3, j // 3)

                if currNum in boxMap[boxCoordinate] or currNum in colsMap[j] or currNum in rowsMap[i]:
                    return False

                boxMap[boxCoordinate].add(currNum)
                colsMap[j].add(currNum)
                rowsMap[i].add(currNum)

        return True
        