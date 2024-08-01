class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def buildTriangle(first, second):
            currHeight = 0
            canBuild = True

            while canBuild:
                if first >= (currHeight + 1):
                    first -= (currHeight + 1)
                    currHeight += 1

                else:
                    canBuild = False
                    break

                if second >= (currHeight + 1):
                    second -= (currHeight + 1)
                    currHeight += 1

                else:
                    canBuild = False

                # print(currHeight, first, second)

            return currHeight

        return max(buildTriangle(red, blue), buildTriangle(blue, red))


        