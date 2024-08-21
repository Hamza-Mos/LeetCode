class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # just group up the list 
        # (startTime, endTime, profit)
        times_and_profits = list(zip(startTime, endTime, profit))

        # sort by startTime
        times_and_profits.sort()

        """
        approach:

        - top-down memoization solution
        - we have 2 choices for each job:
            - skip it and move to next index
            - take it and then call the function on the next valid index
                - next valid index is when the next startTime >= current endTime

        """

        cache = {} # index -> max profit starting at jobs[index:]

        def dfs(index):
            if index in cache:
                return cache[index]

            if index == len(times_and_profits):
                return 0

            skip_job = dfs(index + 1)

            # take job
            start_time, end_time, profit = times_and_profits[index]

            # find next index
            next_index = bisect.bisect_left(times_and_profits, (end_time, -1, -1))

            cache[index] = max(profit + dfs(next_index), skip_job)

            return cache[index]

        return dfs(0)
        