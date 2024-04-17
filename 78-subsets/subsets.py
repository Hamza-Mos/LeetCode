class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currSet = []

        def backtrack(index):
            if index == len(nums):
                res.append(currSet[:])
                return

            # add current number
            currSet.append(nums[index])
            backtrack(index + 1)

            # do not add current number
            currSet.pop()
            backtrack(index + 1)

        backtrack(0)

        return res
        