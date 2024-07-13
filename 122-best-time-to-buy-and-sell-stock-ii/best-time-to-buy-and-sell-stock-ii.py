class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        # keep track of (index, buyingOrSelling)

        def dfs(index, buy):
            if (index, buy) in cache:
                return cache[(index, buy)]

            if index >= len(prices):
                return 0

            skip = dfs(index + 1, buy)
            # res = cooldown

            # buying
            if buy:
                buyingRes = dfs(index + 1, not buy) - prices[index]
                cache[(index, buy)] = max(buyingRes, skip)

            # selling
            else:
                sellingRes = dfs(index + 1, not buy) + prices[index]
                cache[(index, buy)] = max(sellingRes, skip)

            return cache[(index, buy)]

        return max(dfs(0, True), 0)
        