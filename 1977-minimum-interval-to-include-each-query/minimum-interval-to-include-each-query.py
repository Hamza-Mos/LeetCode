class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        intuition for this problem:

            - basically we want to sort both queries and intervals so that queries will be matched up
            closely with intervals (we don't want to check all intervals for each query as some intervals
            will not contain the correct range for the query - so we avoid repeated work that way)

            - to keep track of interval sizes for valid intervals for each query, we will use a minHeap
                - we will keep track of the right pointer for each interval in the minHeap as well so we 
                can remove the intervals that are no longer in the window for the current query
        """

        # sort by left pointer for intervals
        intervals.sort()

        # maps each query to its min interval size (-1 if no valid interval exists)
        queriesToSizes = {}

        intervalIndex = 0 # keeps track of index of current interval we could add to minHeap
        minHeap = []

        for query in sorted(queries):
            # add valid intervals to minHeap
            while intervalIndex < len(intervals) and intervals[intervalIndex][0] <= query:
                left, right = intervals[intervalIndex]

                # minHeap contains pairs of (size of interval, right boundary of interval)
                heapq.heappush(minHeap, (right - left + 1, right))

                # increment index to next interval
                intervalIndex += 1

            # remove invalid intervals from minHeap
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            queriesToSizes[query] = minHeap[0][0] if minHeap else -1

        res = [ queriesToSizes[query] for query in queries ]
        
        return res