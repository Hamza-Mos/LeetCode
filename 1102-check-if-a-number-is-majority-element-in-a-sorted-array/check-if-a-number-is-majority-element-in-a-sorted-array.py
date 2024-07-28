class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # binary search
        n = len(nums)

        # get leftmost index of target
        leftmost = float('inf')

        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                leftmost = min(leftmost, mid)
                hi = mid - 1

            elif nums[mid] > target:
                hi = mid - 1

            else:
                lo = mid + 1

        if leftmost == float('inf'):
            return False

        # get rightmost index of target
        rightmost = float('-inf')

        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                rightmost = max(leftmost, mid)
                lo = mid + 1

            elif nums[mid] > target:
                hi = mid - 1

            else:
                lo = mid + 1

        return (rightmost - leftmost + 1) > n // 2



        