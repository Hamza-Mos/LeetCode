class Solution:
    def countAndSay(self, n: int) -> str:
        currString = "1"

        for i in range(n - 1):
            left = right = 0
            newString = ""

            while left < len(currString):
                while right < len(currString) and currString[left] == currString[right]:
                    right += 1

                currNumLen = right - left

                newString += str(currNumLen) + currString[left]
                left = right

            currString = newString


        return currString
        