class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numSet:
                currLen = 1

                while n + 1 in numSet:
                    n += 1
                    currLen += 1
                res = max(currLen, res)

        return res
        