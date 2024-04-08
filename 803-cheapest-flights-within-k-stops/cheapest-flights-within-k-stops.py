class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n

        # we can start at src location
        prices[src] = 0

        for i in range(k + 1):
            # here is why we need a temp copy of the prices array

            # prices shows the min price it takes to get to a location using (i - 1) intermediate stops

            # tmpPrices will be used to determine min price it takes to get to each location starting from
            # the src location using i intermediate stops (which will be prices[location] + additionalPrice)
            tmpPrices = prices.copy()

            for source, destination, price in flights:
                # we cannot yet reach the src location
                if prices[source] == float('inf'):
                    continue

                # we can reach the src location and thus can reach dest location with additional price
                tmpPrices[destination] = min(tmpPrices[destination], prices[source] + price)

            prices = tmpPrices # update prices array

        return -1 if prices[dst] == float('inf') else prices[dst]