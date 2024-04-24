class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # two states for each number: positive or negative
        # in our dp cache, to keep track of combinations for each number, we need to save the index and current sum

        dp = {} # cache

        def dfs(index, currSum):
            # end of array
            if index == len(nums):
                if currSum == target:
                    return 1

                else:
                    return 0
                    
            if (index, currSum) in dp:
                return dp[(index, currSum)]

            dp[(index, currSum)] = dfs(index + 1, currSum - nums[index]) + dfs(index + 1, currSum + nums[index])

            return dp[(index, currSum)]

        return dfs(0, 0)
        