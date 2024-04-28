class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # instead of tackling this problem by solving subproblems of finding max coins within each subarray, instead
        # we can solve the subproblems of max coins of each subarray by getting number of coins if we pop each
        # element in the subarray as the last balloon

        # we will essentially use a dfs with a left and right pointer outlining the bounds of the subarray, then
        # we will loop through each element in the subarray and get the result of the product of the current element
        # and the elements outside the left and right bounds (because we assume this element will be the last 
        # balloon popped) -> then we add up the result of the recursive calls on the left and right subarrays

        # surround nums with 1's on outsides
        nums = [1] + nums + [1]

        # cache
        dp = {}

        def dfs(left, right):
            # invalid subarray
            if left > right:
                return 0

            if (left, right) in dp:
                return dp[(left, right)]

            maxCoins = 0

            for index in range(left, right + 1):
                currSum = nums[left - 1] * nums[index] * nums[right + 1] + dfs(left, index - 1) + dfs(index + 1, right)
                maxCoins = max(currSum, maxCoins)

            dp[(left, right)] = maxCoins

            return maxCoins

        return dfs(1, len(nums) - 2)
            
        