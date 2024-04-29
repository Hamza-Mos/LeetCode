class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # this question is a followup to leetcode 713 (number of subarrays with product less than k)
        # ^^ make sure you do that question first!!!

        left = 0
        currSum = 0
        res = 0

        # sliding window approach
        for right in range(len(nums)):
            # update sum
            currSum += nums[right]

            # length of current window
            currLen = right - left + 1

            # calculate score
            score = currSum * currLen

            # if current window has a higher score than k then we shrink it from the left
            while left <= right and score >= k:
                currSum -= nums[left]
                left += 1
                currLen -= 1
                score = currSum * currLen 

            # number of subarrays of current window is always equal to the length of the current window
            res += currLen

        return res
        