class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # good solution: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solutions/4261149/very-inituive-solution-with-sorting/

        """
        approach:

            - use a hashmap to count the number of times each array index was included in the current window
            - flatten all lists into a single list and sort it
            - initialize the result range to [smallestNum, largestNum] from the sorted list
            
            - loop over each element in the sorted list, and update the count in the hashmap
            - if the hashmap contains all k lists then do the following:
                - use the sliding window technique, keep shrinking the window from the left
                  until the hashmap no longer includes all k lists
                - update the result range each time to have the shortest range difference

            - return the result range
        """

        k = len(nums)
        numsList = []
        arrCount = defaultdict(int)

        for index, array in enumerate(nums):
            for num in array:
                numsList.append([index, num])

        # sort list and initialize result variables
        numsList.sort(key=lambda x: x[1]) # sort by value not index
        res = [numsList[0][1], numsList[-1][1]]
        resDiff = numsList[-1][1] - numsList[0][1]

        # left pointer in sliding window
        left = 0

        for right, (arrIndex, val) in enumerate(numsList):
            arrCount[arrIndex] += 1

            # shrink window from left
            while len(arrCount) == k:
                lowerBound = numsList[left][1]
                upperBound = val

                # update res
                if upperBound - lowerBound < resDiff:
                    resDiff = upperBound - lowerBound
                    res = [lowerBound, upperBound]

                # remove left val
                indexToRemove = numsList[left][0]
                arrCount[indexToRemove] -= 1

                if arrCount[indexToRemove] == 0:
                    del arrCount[indexToRemove]

                left += 1

        return res
        