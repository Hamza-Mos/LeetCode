class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        approach:

        NOTE: its important to recognize that the solution will always exist in the set {1, ..., len(nums)}

        with that in mind, there are 3 main approaches:

            1) sorting (brute force / naive solution) -> find smallest missing positive using a counter and
               start at 1

            2) convert nums to a hashset and use a counter and start at 1 then return counter if it does not
               exist in the set

            3) optimal: you can mark numbers you have seen before by marking their indices as negative
                - example: given [2, 3, 4]
                    - you can mark that you have seen 2 by making nums[2 - 1] negative

                - NOTE: negative numbers don't matter - you can ignore them by making them 0 to begin with

                - first loop: get rid of negative numbers
                - second loop: mark numbers you have seen by taking their absolute value and making their index 
                  negative. if the number is 0, then mark it as negative by setting it to -1 * (len(nums) + 1)
                  since len(nums) + 1 is not part of the solution set anyways (invalid index) and would not
                  affect our result

                - third loop: loop over all elements in the solution set (1 -> len(nums)) and find the first
                  number whose index is not negative (means it is missing)

        time: O(N)
        space: O(1)

        """

        # first loop: get rid of negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # second loop: mark numbers that part of the solution set as seen
        for i in range(len(nums)):
            # we take absolute because it is possible that this number was set to negative previously
            # which would mean that the number (i + 1) was seen before
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                index = val - 1
                
                # value is 0, set it to negative out of bounds number
                if nums[index] == 0:
                    nums[index] = -1 * (len(nums) + 1)

                # value is positive, set to negative
                elif nums[index] > 0:
                    nums[index] = -1 * nums[index]

        # third loop - find result

        for i in range(1, len(nums) + 1):
            # if nums[i - 1] is not negative, then we have not seen it before in the list
            if nums[i - 1] >= 0:
                return i

        # we have seen all numbers in {1, ..., len(nums)} so len(nums) + 1 must be the answer
        return len(nums) + 1
        