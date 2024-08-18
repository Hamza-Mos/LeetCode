class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numCount = defaultdict(int)
        res = 0

        for n in nums:
            res += numCount[n]
            numCount[n] += 1

        return res

        