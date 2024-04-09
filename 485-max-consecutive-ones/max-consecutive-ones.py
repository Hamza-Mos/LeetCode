class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        longest = 0

        for n in nums:
            if n == 0:
                curr = 0

            else:
                curr += 1

            longest = max(longest, curr)

        return longest
        