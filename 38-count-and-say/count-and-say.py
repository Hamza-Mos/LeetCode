class Solution:
    def countAndSay(self, n: int) -> str:
        # base string
        currString = "1"

        for i in range(n - 1):
            # two pointer approach
            # left ptr points to current number we are looking at
            # right pointer stretches as far outward until the characters on the left and right no longer match
            left = right = 0

            # new string we form in the current iteration of the loop
            newString = ""

            while left < len(currString):
                # find consecutive sequence of number chars
                while right < len(currString) and currString[left] == currString[right]:
                    right += 1

                # length of current sequence
                currNumLen = right - left

                # to add the new sequence, we add the length of it and then the actual number char
                newString += str(currNumLen) + currString[left]

                # update left ptr for next window
                left = right

            # update current string
            currString = newString


        return currString
        