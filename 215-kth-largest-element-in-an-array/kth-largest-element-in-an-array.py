class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        approach:

        - edge case: check if k > len(nums), if true, then return 0

        - min heap of size k
            - populate the heap with the first k elements in nums

            - iterate through the rest of the array, 
                - if the current element > top of the heap, then pop, and add that number to heap

        - return minHeap[0]

        """

        # edge case
        if k > len(nums):
            return 0

        minHeap = nums[:k]
        heapq.heapify(minHeap)


        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])

        return minHeap[0]
        