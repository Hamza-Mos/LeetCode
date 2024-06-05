class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # [3,5,2,3]
        # biggest numbers are paired with smallest numbers
        # [2, 3, 3, 5]
        #       i
        # 2 -> 5
        # 3 -> 3
        nums.sort()
        maxSum = 0

        for i in range(len(nums) // 2):
            maxSum = max(maxSum, nums[i] + nums[len(nums) - 1 - i])

        return maxSum