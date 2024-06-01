class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # decreasing monotonic queue
        res = []

        q = deque()

        for i in range(k):
            while q and q[-1][1] < nums[i]:
                q.pop()

            q.append([i, nums[i]])

        res.append(q[0][1])

        for i in range(k, len(nums)):
            while q and q[0][0] <= i - k:
                q.popleft()

            while q and q[-1][1] < nums[i]:
                q.pop()

            q.append([i, nums[i]])

            res.append(q[0][1])

        return res
        