class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers to easily manage duplicates
        nums.sort()
        
        res = []
        currSet = []

        def backtrack(index):
            if index == len(nums):
                res.append(currSet[:])
                return

            # add current number
            currSet.append(nums[index])
            backtrack(index + 1)

            # remove all instances of nums[index] (duplicates)
            currSet.pop()

            # now nums[index] will point to last occurrence of that number
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # index + 1 will point to next unique number (or end of array)
            backtrack(index + 1)

        backtrack(0)

        return res
        