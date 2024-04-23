class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so at each stage - we have a choice between buying or selling or cooldown (3 choices)
        # if we buy then we proceed to next index and subtract our current profit amount by prices[i]
        # if we sell then we skip next index and move to (i + 2) b/c of cooldown + prices[i]
        # we always have a choice of cooldown which is where our current profit is unchanged and we move to (i + 1)

        dp = {} # cache
        

        # buying is a boolean (true or false)
        # index is current index we are on
        def getMaxProfit(buying, index):
            if (buying, index) in dp:
                return dp[(buying, index)]

            if index >= len(prices):
                return 0

            # cooldown
            cooldown = getMaxProfit(buying, index + 1)
            maxProfit = 0

            # buying
            if buying:
                maxProfit = getMaxProfit(False, index + 1) - prices[index]

            # selling
            else:
                maxProfit = getMaxProfit(True, index + 2) + prices[index]

            dp[(buying, index)] = max(maxProfit, cooldown)
            return dp[(buying, index)]

        return getMaxProfit(True, 0)