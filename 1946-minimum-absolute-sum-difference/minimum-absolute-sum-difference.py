class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        diffSum = sum(abs(num1 - num2) for num1, num2 in zip(nums1, nums2))
        maxSumDiff = 0

        sortedNums = sorted(nums1)
        n = len(nums1)

        for num1, num2 in zip(nums1, nums2):
            closestNumIndex = bisect.bisect_left(sortedNums, num2)

            # we should try both closestNumIndex and closestNumIndex - 1
            # edge case: [1, 2, 3, 100] and 4 -> closestNumIndex would point to 100
            oldDiff = abs(num1 - num2)
            newDiff = oldDiff

            if closestNumIndex == 0:
                newDiff = abs(sortedNums[0] - num2)

            elif closestNumIndex == n:
                newDiff = abs(sortedNums[-1] - num2)

            else:
                newDiff = min(abs(sortedNums[closestNumIndex - 1] - num2), abs(sortedNums[closestNumIndex] - num2))            

            maxSumDiff = max(maxSumDiff, oldDiff - newDiff)

        return (diffSum - maxSumDiff) % MOD




        