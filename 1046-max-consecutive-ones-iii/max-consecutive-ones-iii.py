class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxStreak = 0
        left = 0
        numOnes = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                numOnes += 1

            while (right - left + 1) - numOnes > k:
                print([left, right])
                if nums[left] == 1:
                    numOnes -= 1

                left += 1

            maxStreak = max((right - left + 1), maxStreak)

        return maxStreak
        