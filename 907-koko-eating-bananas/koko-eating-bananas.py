class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def getHours(numBananasPerHour):
            hours = 0

            for p in piles:
                hours += math.ceil(p / numBananasPerHour)

            return hours

        res = float('inf')

        while low <= high:
            mid = (low + high) // 2

            numHours = getHours(mid)

            if numHours <= h:
                res = min(res, mid)
                
                # continue to eat less
                high = mid - 1


            # invalid - need to eat more
            else:
                low = mid + 1

        return res
        