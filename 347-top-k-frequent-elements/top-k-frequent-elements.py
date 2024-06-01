class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        buckets = collections.defaultdict(list)

        for num, frequency in freq.items():
            buckets[frequency].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            if len(res) == k:
                return res

            res.extend(buckets[i])

        return res
        