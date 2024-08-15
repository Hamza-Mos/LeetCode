class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)

        if totalSum % k != 0:
            return False

        # sum per each partition
        targetSum = totalSum // k

        # use bit masking to track whether or not a number is taken
        # ex: 101 for [5, 6, 7] indicates that 5 and 7 were already taken in prev/current partitions

        # sort in reverse order
        # basically if any number is larger than the targetSum then we know its impossible
        nums.sort(reverse=True)

        cache = {} # contains mask as key and boolean values
        mask = 0

        def backtrack(index, numSubsets, currSum):
            nonlocal mask

            if mask in cache:
                return cache[mask]

            if numSubsets == k:
                return True

            if currSum > targetSum:
                return False

            # base case
            if currSum == targetSum:
                # start from beginning of array since its not guaranteed that we pick
                # elements in sequential order
                cache[mask] = backtrack(0, numSubsets + 1, 0)
                return cache[mask]

            # find element to include in current subset
            for i in range(index, len(nums)):
                # check if current element is not taken
                if ((mask >> i) & 1) == 0:
                    # include this element as part of current set
                    mask = (mask | 1 << i) 

                    if backtrack(i + 1, numSubsets, currSum + nums[i]):
                        return True

                    # backtrack
                    mask = (mask ^ (1 << i))

            cache[mask] = False

            return cache[mask]

        return backtrack(0, 0, 0)

        
        