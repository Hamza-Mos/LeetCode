class Solution:
    def rob(self, nums: List[int]) -> int:
        robCurrHouseAndOne = 0
        doNotRobCurrHouse = nums[-1]

        # need a variable for dp[i] (temp), dp[i + 1] (doNotRobCurrHouse), and dp[i + 2] (robCurrHouseAndOne)
        # dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        for i in reversed(range(len(nums) - 1)):
            temp = max(robCurrHouseAndOne + nums[i], doNotRobCurrHouse)
            robCurrHouseAndOne = doNotRobCurrHouse
            doNotRobCurrHouse = temp

        return doNotRobCurrHouse
        