class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # decreasing monotonic stack??
        ans = longestPeriod = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                longestPeriod += 1
            else:
                longestPeriod = 1
                
            ans += longestPeriod

        return ans
        