class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        res = 0

        def countRibbons(cutLength):
            count = 0
            for ribbon in ribbons:
                count += ribbon // cutLength

            return count

        while left <= right:
            mid = (left + right) // 2

            count = countRibbons(mid)

            # valid answer - can try cutting more (more greedy)
            if count >= k:
                res = max(mid, res)
                left = mid + 1

            # invalid - need to cut less
            else:
                right = mid - 1

        return res
        