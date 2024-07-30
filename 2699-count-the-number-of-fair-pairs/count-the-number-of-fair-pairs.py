class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # loop over each number and identify the upper bound and lower bound for each number (Binary search)
        res = 0
        nums.sort()

        for i in range(len(nums) - 1):
            low = i + 1
            high = len(nums) - 1

            # upper bound
            upperBound = float('-inf')

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] + nums[i] <= upper:
                    upperBound = max(upperBound, mid)
                    low = mid + 1

                else:
                    high = mid - 1

            # lower bound
            lowerBound = float('inf')

            low = i + 1
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] + nums[i] >= lower:
                    lowerBound = min(lowerBound, mid)
                    high = mid - 1

                else:
                    low = mid + 1

            if upperBound == float('-inf') or lowerBound == float('inf'):
                continue

            res += (upperBound - lowerBound + 1)

        return res


        