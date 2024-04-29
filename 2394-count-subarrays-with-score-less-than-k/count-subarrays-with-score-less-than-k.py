class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # this question is a followup to leetcode 713 (number of subarrays with product less than k)

        left = 0
        currSum = 0
        res = 0

        for right in range(len(nums)):
            currSum += nums[right]
            currLen = right - left + 1
            score = currSum * currLen

            while left <= right and score >= k:
                currSum -= nums[left]
                left += 1
                currLen -= 1
                score = currSum * currLen 

            res += currLen

        return res
        