class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNum = len(nums)

        for i in range(len(nums)):
            missingNum = missingNum ^ (i ^ nums[i])

        return missingNum
        