class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort by starting?
        pairs.sort()

        # dp[i] represents the longest chain starting at the ith index

        dp = [1] * len(pairs)
        res = 1

        for i in range(len(pairs) - 1, -1, -1):
            for j in range(i + 1, len(pairs)):
                # check if these pairs form a chain
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

            res = max(res, dp[i])

        return res
        