class Solution:
    def position(self, nums, m):
        ans = 0
        for i in range(len(nums) - 1):
            index = bisect.bisect_left(nums, nums[i] + m + 1)
            ans += (index - 1 - i)
        return ans

    def smallestDistancePair(self, nums, k):
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while r - l > 1:
            m = l + (r - l) // 2
            if self.position(nums, m) >= k:
                r = m
            else:
                l = m
        if self.position(nums, l) >= k:
            return l
        elif self.position(nums, r) >= k:
            return r
        return 0