class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # 1) find number of subarrays where max element is <= right
        # 2) find number of subarrays where max element is <= left - 1
        # 3) subtract the 2 numbers to get number of subarrays where max element is between both bounds

        # step 1
        currCount = 0
        lessThanRightCount = 0

        for n in nums:
            currCount = currCount + 1 if n <= right else 0
            lessThanRightCount += currCount

        # step 2
        currCount = 0
        lessThanLeftCount = 0

        for n in nums:
            currCount = currCount + 1 if n <= left - 1 else 0
            lessThanLeftCount += currCount

        # step 3
        return lessThanRightCount - lessThanLeftCount