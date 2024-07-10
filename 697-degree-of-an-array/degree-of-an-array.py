class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxFreq = max(freq.values())

        l = 0
        subarrayFreq = defaultdict(int)
        windowFreq = 0
        res = len(nums)

        for r in range(len(nums)):
            num = nums[r]
            subarrayFreq[num] += 1

            while subarrayFreq[num] == maxFreq:
                leftNum = nums[l]
                res = min(res, r - l + 1)
                subarrayFreq[leftNum] -= 1
                l += 1

        return res
        