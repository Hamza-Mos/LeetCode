class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curr] = nums[i]
                curr += 1

        return curr
        