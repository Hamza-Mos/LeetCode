class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # greedy
        tapRanges = [0] * (n + 1)

        for i in range(n + 1):
            tapStart = max(0, i - ranges[i])
            tapEnd = min(n, i + ranges[i])

            tapRanges[tapStart] = max(tapRanges[tapStart], tapEnd)

        # problem is now similar to jump game 2
        # where tapRanges[i] represents the max jump you can make from the ith index
        numTaps = 0
        currEnd = 0 # last index you can reach from last tap chosen
        maxEnd = 0 # max index you can reach with all visited taps so far

        for i in range(n + 1):
            # impossible to reach end of garden
            if i > maxEnd:
                return -1

            if i > currEnd:
                currEnd = maxEnd
                numTaps += 1

            maxEnd = max(maxEnd, tapRanges[i])

        return numTaps

        