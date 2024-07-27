class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford algo
        prices = [float('inf')] * n
        prices[src] = 0


        # k + 1 because 0 is no stops, last iteration of loop will have k stops
        for i in range(k + 1):
            pricesTemp = prices.copy()

            for s, d, dist in flights:
                # impossible to reach src
                if prices[s] == float('inf'):
                    continue

                pricesTemp[d] = min(pricesTemp[d], prices[s] + dist)

            prices = pricesTemp

        return prices[dst] if prices[dst] != float('inf') else -1
        