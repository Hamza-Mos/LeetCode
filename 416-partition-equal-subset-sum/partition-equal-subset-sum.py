class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        # odd total sum (not divisible by 2)
        if totalSum % 2:
            return False   

        targetSum = totalSum // 2

        # dp[i] is True if we can create a subset with sum of i, False otherwise
        dp = [False] * (targetSum + 1)
        dp[0] = True

        currSum = 0

        for n in nums:
            for i in range(targetSum, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]

        print(dp)


        return dp[targetSum]