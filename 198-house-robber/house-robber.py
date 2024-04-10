class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[-2] = nums[-1]

        for i in reversed(range(len(nums) - 1)):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]
        