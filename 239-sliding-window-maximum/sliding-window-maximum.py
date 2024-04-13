class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue
        q = deque() # will contain (num, index)
        res = []

        for i in range(k):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            
            q.append((nums[i], i))

        res.append(q[0][0])

        for i in range(k, len(nums)):
            # pop elements that are out of the current window
            while q and q[0][1] <= i - k:
                q.popleft()

            # keep queue monotonically decreasing
            while q and q[-1][0] <= nums[i]:
                q.pop()

            q.append((nums[i], i))

            res.append(q[0][0])

        return res
            