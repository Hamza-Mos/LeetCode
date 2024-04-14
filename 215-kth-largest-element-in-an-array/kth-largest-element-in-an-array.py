class Solution:
    def quickSelectSolution(self, nums, k):
        kthIndex = len(nums) - k

        def quickselect(start, end):
            pivot = end
            left = start

            for i in range(start, end):
                if nums[i] <= nums[pivot]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            # swap value at left index with pivot
            nums[left], nums[pivot] = nums[pivot], nums[left]

            # left is now the new index of the pivot value

            # need to do quick select on left portion of the array
            if left > kthIndex:
                return quickselect(start, left - 1)

            # need to do quick select on right portion of the array
            elif left < kthIndex:
                return quickselect(left + 1, end)

            # pivot marks the correct index
            else:
                return nums[left]

        return quickselect(0, len(nums) - 1)

    def heapSolution(self, nums, k):
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heapSolution(nums, k)
        