class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = dp[i + 1] or dp[i + 2] + nums[i]
        if len(nums) <= 2:
            return max(nums)

        robCurrHouse = nums[-1] # dp[i + 2] + nums[i]
        skipCurrHouse = max(nums[-2], nums[-1]) # dp[i + 1]

        for i in range(len(nums) - 3, -1, -1):
            temp = max(robCurrHouse + nums[i], skipCurrHouse)
            robCurrHouse = skipCurrHouse
            skipCurrHouse = temp

        # [2, 1, 1, 2]
        # temp: 3
        # robCurrHouse: 1
        # skipCurrHouse: 3

        return skipCurrHouse
        