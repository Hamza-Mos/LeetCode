class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        approach:

        - use 2 queues (could also use 2 heaps [min heap and max heap] but its less efficient)
            - 1 queue is monontonically increasing (contains min values)
            - other queue is monotonically decreasing (contains max values)

        - use sliding window - keep expanding window until diff between max and min > limit
            - if limit is violatd, then shrink window from left and update the queue accordingly

        """

        minQueue = deque() # monotonically increasing (contains [index, val])
        maxQueue = deque() # monotonically decreasing (contains [index, val])
        res = 0 # max length of subarray
        left = 0

        for right, num in enumerate(nums):
            # indices outside of window
            if minQueue and minQueue[0][0] < left:
                minQueue.popleft()

            if maxQueue and maxQueue[0][0] < left:
                maxQueue.popleft()
            
            # update queues
            while minQueue and minQueue[-1][1] > num:
                minQueue.pop()

            while maxQueue and maxQueue[-1][1] < num:
                maxQueue.pop()

            # add number to queues
            minQueue.append([right, num])
            maxQueue.append([right, num])

            minVal, maxVal = minQueue[0][1], maxQueue[0][1]

            # check if limit is violated
            while maxVal - minVal > limit:
                left += 1

                # indices outside of window
                if minQueue and minQueue[0][0] < left:
                    minQueue.popleft()

                if maxQueue and maxQueue[0][0] < left:
                    maxQueue.popleft()
                
                minVal, maxVal = minQueue[0][1], maxQueue[0][1]

            res = max(res, right - left + 1)

        return res
        