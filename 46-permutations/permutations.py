class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index):
            if index == len(nums):
                res.append(nums[:]) # copy
                return

            # swap all numbers starting at index with every other position
            for i in range(index, len(nums)):
                # swap with number at index
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)

                # backtrack
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0)

        return res
