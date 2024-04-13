class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxStreak = 0
        left = 0
        currStreak = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                currStreak += 1

            while (right - left + 1) - currStreak > k:
                print([left, right])
                if nums[left] == 1:
                    currStreak -= 1

                left += 1

            maxStreak = max((right - left + 1), maxStreak)

        return maxStreak
        