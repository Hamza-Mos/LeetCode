class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use XOR
        # ex: (0 ^ 0) ^ (1 ^ 1) ^ 2 = (0) ^ (0) ^ 2 = 2
        missingNum = len(nums)

        for i in range(len(nums)):
            missingNum = missingNum ^ (i ^ nums[i])

        return missingNum
        