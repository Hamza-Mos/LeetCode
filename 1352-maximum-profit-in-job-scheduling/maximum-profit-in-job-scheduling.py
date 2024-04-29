class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # all jobs sorted by startTime
        jobs = sorted(zip(startTime, endTime, profit))

        # dp cache
        cache = {}

        def dfs(index):
            if index >= len(jobs):
                return 0

            # check cache
            if index in cache:
                return cache[index]

            # profit from skipping current job
            skipJob = dfs(index + 1)

            start, end, profit = jobs[index]

            # profit of scheduling current job
            takeJob = profit

            # find next non conflicting job
            nextJobIndex = bisect.bisect_left(jobs, (end, -1, -1))

            takeJob += dfs(nextJobIndex)

            cache[index] = max(takeJob, skipJob)

            return cache[index]

        return dfs(0)