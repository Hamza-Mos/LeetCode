class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = float('-inf')

        # kadane's algo
        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            res = max(curSum, res)

        return res
        