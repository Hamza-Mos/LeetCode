class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourceChars = set(source)

        # if source does not contain all characters required to create target
        for char in target:
            if char not in sourceChars:
                return -1

        sourcePtr = 0
        count = 0

        for char in target:
            # loop until you can match characters
            while source[sourcePtr] != char:
                sourcePtr += 1
                
                # loop around to start of source (increment count of subsequences too)
                if sourcePtr == len(source):
                    count += 1
                    sourcePtr = 0

            sourcePtr += 1

            if sourcePtr == len(source):
                    count += 1
                    sourcePtr = 0

        return count if sourcePtr == 0 else count + 1
        