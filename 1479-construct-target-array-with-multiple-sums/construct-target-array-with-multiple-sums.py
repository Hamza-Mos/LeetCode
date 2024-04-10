class Solution:
    def isPossible(self, target: List[int]) -> bool:
        totalSum = sum(target)

        maxHeap = [-t for t in target]
        heapq.heapify(maxHeap)

        while -maxHeap[0] > 1:
            print(maxHeap)
            largest = -heapq.heappop(maxHeap)
            rest = totalSum - largest

            if rest == 0:
                return False

            if rest == 1:
                return True

            newVal = largest % rest

            # impossible
            if newVal == 0 or newVal == largest:
                return False

            totalSum = newVal + rest

            heapq.heappush(maxHeap, -newVal)

        return True