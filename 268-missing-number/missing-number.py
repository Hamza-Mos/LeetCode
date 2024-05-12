class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numberSum = 0
        indexSum = len(nums)

        for i in range(len(nums)):
            indexSum += i
            numberSum += nums[i]

        return indexSum - numberSum
        