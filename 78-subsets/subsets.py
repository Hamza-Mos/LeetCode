class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, currSet):
            if index == len(nums):
                res.append(currSet[::])
                return

            currSet.append(nums[index])
            dfs(index + 1, currSet)

            currSet.pop()
            dfs(index + 1, currSet)

        dfs(0, [])
        return res
        