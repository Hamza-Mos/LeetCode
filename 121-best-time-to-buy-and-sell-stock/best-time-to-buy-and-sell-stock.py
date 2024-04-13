class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]

            if profit < 0:
                left = right
                continue

            res = max(res, profit)

        return res
        