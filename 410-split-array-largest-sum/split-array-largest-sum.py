class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # use binary search on [max(nums), sum(nums)] to find max sum of each subarray
        # find min sum of each subarray (greedily)
        # time complexity is (N * log S) where S is sum(nums)

        def getNumSubarrays(subarraySum):
            res = 1 # starts as 1 big subarray
            currSum = 0

            for n in nums:
                currSum += n

                if currSum > subarraySum:
                    currSum = n
                    res += 1

            return res


        low, high = max(nums), sum(nums)
        res = float('inf')

        while low <= high:
            mid = (low + high) // 2
            numSubarrays = getNumSubarrays(mid)
            print(mid, numSubarrays)

            if numSubarrays <= k: # valid case
                res = min(res, mid)
                high = mid - 1 # keep minimizing sum

            else: # sum is too low (too easy to pass threshold)
                low = mid + 1


        return res

