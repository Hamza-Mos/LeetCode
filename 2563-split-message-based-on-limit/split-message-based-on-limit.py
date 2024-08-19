class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        """
        approach:

        - find the count of parts that are appropriate for splitting the message
            - let's define a few variables:
                - partCount: count of parts that the message will be split into. e.g. 'b' in "a/b"
                - totalIndicesLength: the sum of indices of all parts in the array. e.g. all the a's in "a/b"
                  summed up (this is important when splitting the full message into parts)

            - define a variable called digitCount which returns the length of the number as a string

            - basically we want a partCount such that the following condition is satisfied:
                partCount * (3 + digitCount(partCount)) + totalIndicesLength + len(message) <= partCount * limit

                (total number of </b>'s) + (total sum of all a's) + (length of full message) <= (full length of split message)

                (if this condition is not satisfied then current number of parts is not enough)

        - once the count of parts is found, then all is left is splitting the message
            - define an empty parts array (parts = [])
            - define a variable called availableLength which will track how much of the message we can extract
              for each part

            - availableLength = limit - (currentPart + 3 + digitCount(partCount))

            - extract availableLength size from the message in each iteration then append the suffix to the 
              end of the current part

        - return parts array

        - follow up could maybe use binary search for this logic to find smallest number that satisfies:
            partCount * (3 + digitCount(partCount)) + totalIndicesLength + len(message) <= partCount * limit

            (total number of </b>'s) + (total sum of all a's) + (length of full message) <= (full length of split message)

        time: O(N)
        space: O(1)

        """

        def digitCount(number):
            return len(str(number))

        partCount = totalIndicesLen = 1 # counting num parts, sum of part indices

        # find suitable partCount
        while partCount * (3 + digitCount(partCount)) + totalIndicesLen + len(message) > limit * partCount:
            # <b/b> where b = partCount
            # impossible
            if 2 * digitCount(partCount) + 3 >= limit:
                return []

            partCount += 1
            totalIndicesLen += digitCount(partCount)

        # build parts array
        parts = []

        # indices are 1-indexed
        for index in range(1, partCount + 1):
            availableLength = limit - (3 + digitCount(index) + digitCount(partCount)) # limit - len(<a/b>)

            # extract current part and remove it from the message
            currPart = message[:availableLength]
            message = message[availableLength:]

            part = f"{currPart}<{index}/{partCount}>"
            parts.append(part)

        return parts

        